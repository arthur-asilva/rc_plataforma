from django.shortcuts import redirect, render, HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.conf import settings
from Apps.tools.views import encode, decode, uploadArquivo, AuthValidation
from Apps.tutoriais.models import Complemento, Tutorial
from Apps.usuarios.views import auth
from django.core.files.storage import FileSystemStorage
from unidecode import unidecode




def TutoriaisView(request):
    id = request.GET.get('id', None)
    turma = int(decode(request.GET.get('t', None)))
    material = request.GET.get('data', None)
    tutoriais = Tutorial.objects.filter(turma=turma).order_by('indice')

    if material != None and id != None:
        material = decode(request.GET['data'])
        id = int(decode(request.GET['id']))

    data = {
        'id': id,
        'material': material,
        'tutoriais': tutoriais,
        'turma': turma,
    }
    return render(request, 'tutoriais/tutoriais.html', data)


@AuthValidation
def TutoriaisCadastroView(request):

    editar = request.GET.get('id', None)
    plano_1 = request.FILES.get('plano_1', None)
    plano_2 = request.FILES.get('plano_2', None)
    programacao = request.FILES.get('programacao', None)
    turma = request.GET['t']
    url = None
    material = Tutorial()
    total_por_turma = Tutorial.objects.filter(turma=decode(turma)).count() + 1

    if editar != None:
        material = Tutorial.objects.get(id=decode(editar))

    if request.method == 'POST':
        url = 'Tutoriais/' + request.POST['turma'] + '/' + unidecode(request.POST['nome'])
        material.indice = request.POST['indice']
        material.turma = request.POST['turma']
        material.nome = request.POST['nome']
        material.video = request.POST['video']

        if plano_1 is not None:
            material.plano_1 = uploadArquivo(plano_1, url + '/plano_tecnico')
        if plano_2 is not None:
            material.plano_2 = uploadArquivo(plano_2, url + '/plano_propedeutico')
        if programacao is not None:
            material.programacao = uploadArquivo(programacao, url + '/programacao')

        material.save()

    data = {
        'turmas': settings.TURMAS,
        'turma': turma,
        'material': material,
        'turma_sel': int(decode(request.GET['t'])),
        'total_por_turma': total_por_turma
    }

    return render(request, 'tutoriais/cadastro.html', data)


@xframe_options_exempt
def TutoriaisComplementoView(request):
    tutorial = int(decode(request.GET['t']))
    tutorial = Tutorial.objects.get(id=tutorial)
    complementos = Complemento.objects.filter(tutorial__id=tutorial.id)
    material = None

    if request.GET.get('c', None) != None:
        material = Complemento.objects.get(id=int(decode(request.GET['c'])))

    data = {
        'turma': int(tutorial.turma),
        'tutorial': tutorial,
        'complementos': complementos,
        'material': material
    }

    return render(request, 'tutoriais/complementos.html', data)



@AuthValidation
def CadastroComplementoView(request):
    tutorial = int(decode(request.GET['t']))
    tutorial = Tutorial.objects.get(id=tutorial)
    anexo = request.FILES.get('anexo', None)
    url = 'Tutoriais/' + tutorial.nome + '/Complementos/' + unidecode(request.POST['nome'])

    if request.method == 'POST':
        complemento = Complemento()
        complemento.nome = request.POST['nome']
        complemento.video = request.POST['video']
        complemento.descricao = request.POST['descricao']
        complemento.tutorial = tutorial
        complemento.postado_por = auth(request)

        if anexo is not None:
            fss = FileSystemStorage()
            url = url + 'complemento.' + anexo.name.split('.')[-1]
            upload = fss.save(url, anexo)
            complemento.arquivo = fss.url(upload)
        
        complemento.save()

    data = {
        'turma': int(tutorial.turma),
        'tutorial': tutorial
    }
    return render(request, 'tutoriais/cadastro_complemento.html', data)




@AuthValidation
def TutoriaisDeleteView(request):
    tutorial = int(decode(request.GET['id']))
    tutorial = Tutorial.objects.get(id=tutorial)
    tutorial.delete()
    return redirect('../tutoriais/?t=' + request.GET['t'])