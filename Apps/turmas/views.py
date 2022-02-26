from django.shortcuts import render, redirect
from Apps.turmas.models import Unidade, Escola, Turma
from Apps.usuarios.models import Usuario
from django.conf import settings
from Apps.tools.views import AuthValidation


@AuthValidation
def CadastroTurmaView(request):

    escola_add = request.POST.get('escola_add', None)
    turma_add = request.POST.get('turma_add', None)
    aba = int(request.GET.get('e', 1))
    turma = Turma()
    escola = Escola()
    editar = request.GET.get('id', None)
    
    if editar != None and aba == 1:
        editar = Escola.objects.get(id=request.GET['id'])
        escola = editar
    if editar != None and aba == 0:
        editar = Turma.objects.get(id=request.GET['id'])
        turma = editar

    if request.method == 'POST':
        if escola_add != None:
            escola.nome = request.POST['nome']
            escola.unidade = Unidade.objects.get(id=request.POST['turma'])
            escola.endereco = request.POST['endereco']
            escola.responsavel = request.POST['nome_responsavel']
            escola.contato = request.POST['contato']
            escola.save()
            return redirect('../add_turma/?e=1')
        if turma_add != None:
            turma.nome = request.POST['turma']
            turma.turno = request.POST['turno']
            turma.escola = Escola.objects.get(id=request.POST['escola'])
            turma.professor = Usuario.objects.get(id=request.POST['professor'])
            turma.quantidade_alunos = request.POST['quantidade']
            turma.save()
            return redirect('../add_turma/?e=0')

    data = {
        'aba': aba,
        'unidades': Unidade.objects.all().order_by('estado', 'cidade'),
        'turmas': settings.TURMAS,
        'escolas': Escola.objects.all(),
        'turmas_cadastradas': Turma.objects.all(),
        'professores': Usuario.objects.all(),
        'editar': editar
    }
    return render(request, 'turmas/cadastros.html', data)