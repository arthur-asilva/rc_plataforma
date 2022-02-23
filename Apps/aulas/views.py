from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from Apps.turmas.models import Turma
from Apps.usuarios.models import Usuario
from Apps.usuarios.views import auth
from Apps.tools.views import decode
from Apps.tools.data_choices import CLASS_SHIFTS, CLASS_SEGMENTS, CLASS_PLAIN_EMPHASIS, classesPerSegments
from .models import Planejamento, Resposta
import csv, datetime, base64
from io import StringIO

def PlanejamentosView(request):

    respostas = getRespostas(request, 0)

    data = {
        'planejamentos': respostas,
        'respondidos': respostas.count(),
        'recebidos': Planejamento.objects.filter(visto=False),
        'turmas': Turma.objects.filter(professor__id=auth(request).id).count() == 0
    }

    return render(request, 'aulas/planejamentos.html', data)


def PlanejamentoRespostaView(request):

    planejamento = int(decode(request.GET['p']))
    respostas = getRespostas(request, 0)

    if request.method == 'POST':
        resposta = Resposta()
        resposta.planejamento = Planejamento.objects.get(id=int(request.POST['planejamento']))
        resposta.mensagem = request.POST['mensagem']
        resposta.usuario = Usuario.objects.get(id=auth(request).id)
        resposta.save()
        return redirect('../planejamentos/')

    data = {
        'planejamento': Planejamento.objects.get(id=planejamento),
        'respostas': Resposta.objects.filter(planejamento__id=planejamento).order_by('-data'),
        'respondidos': respostas.count(),
        'recebidos': Planejamento.objects.filter(visto=False)
    }
    return render(request, 'aulas/responder.html', data)


def NovoPlanejamentoView(request):
    professor = Usuario.objects.get(id=auth(request).id)
    respostas = getRespostas(request, 0)
    turmas = None
    planilha_modelo = None
    dia_aula = None

    if request.method == 'POST':
        filtro = {
            'escola__id': request.POST['escola'],
            'turno': request.POST['turno'],
            'nome__in': classesPerSegments(request.POST['segmento']),
            'professor__id': professor.id
        }
        turmas = Turma.objects.filter(**filtro)
        dia_aula = datetime.datetime.fromisoformat(request.POST['data'])

        data = [['id', 'turma', 'enfase(T/F)', 'tema', 'objetivo', 'data']]

        for turma in turmas:
            for i in range(4):
                date = dia_aula + datetime.timedelta(days=(i * 7) )
                data.append([turma.id, turma.nome, '', '', '', date.strftime('%Y-%m-%d')])
            
        with open(f'{request.session["auth_session"]}.csv', 'w', encoding='UTF8') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerows(data)

        file = open(f'{request.session["auth_session"]}.csv', 'r')
        planilha_modelo = base64.b64encode(file.read().encode('utf-8')).decode("utf-8")

        # return redirect('../planejamentos/')

    data = {
        'escolas': Turma.objects.values('escola__nome', 'escola__id').filter( professor__id=auth(request).id ),
        'turnos': CLASS_SHIFTS,
        'segmentos_aula': CLASS_SEGMENTS,
        'respondidos': respostas.count(),
        'recebidos': Planejamento.objects.filter(visto=False),
        'enfases': CLASS_PLAIN_EMPHASIS,
        'turmas': turmas,
        'dia_aula': dia_aula,
        'planilha_modelo': planilha_modelo
    }

    return render(request, 'aulas/novo_planejamento.html', data)



def VisualizarView(request):
    planejamento = int(decode(request.GET['p']))

    Resposta.objects.filter(planejamento__id=planejamento, visto=False).update(visto=True)

    if auth(request).grupo.nome == 'administrador':
        respostas = Resposta.objects.filter(visto=False).order_by('-planejamento__data_envio')
        Planejamento.objects.filter(id=planejamento, visto=False).update(visto=True)
    else:
        respostas = Resposta.objects.filter(planejamento__usuario__id=auth(request).id, visto=False).order_by(
            '-planejamento__data_envio')

    data = {
        'planejamento': Planejamento.objects.get(id=planejamento),
        'respostas': Resposta.objects.filter(planejamento__id=planejamento).order_by('-data'),
        'respondidos': respostas.count(),
        'recebidos': Planejamento.objects.filter(visto=False)
    }
    return render(request, 'aulas/visualizar.html', data)


def EnviadosView(request):
    respostas = getRespostas(request, 0)
    planejamentos = getRespostas(request, 1)

    data = {
        'planejamentos': planejamentos,
        'respondidos': respostas.count(),
        'recebidos': Planejamento.objects.filter(visto=False)
    }

    return render(request, 'aulas/enviados.html', data)


def getRespostas(request, indice):
    result = {}
    if auth(request).grupo.nome == 'administrador':
        result[0] = Resposta.objects.filter(visto=False).order_by('-planejamento__data_envio')
        result[1] = Planejamento.objects.all().order_by('-data_envio')
    else:
        result[0] = Resposta.objects.filter(planejamento__usuario__id=auth(request).id, visto=False).order_by(
            '-planejamento__data_envio')
        result[1] = Planejamento.objects.filter(usuario__id=auth(request).id).order_by('-data_envio')
    return result[indice]