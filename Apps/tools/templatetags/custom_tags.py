from django import template
import datetime
# import json

from Apps.usuarios.models import Usuario
# from Apps.contatos.models import Chat
from Apps.usuarios.views import auth
from Apps.aulas.models import GradePlanComment
from django.conf import settings
from Apps.tools.views import encode, decode

register = template.Library()



@register.filter(name='encodeDecode')
def encodeDecode(value, args):
    mensagem = value
    if args == 'encode':
        mensagem = encode(value)
    else:
        mensagem = decode(value)
    return mensagem


@register.filter(name='weekDate')
def weekDate(value, args):
    date = None
    if args > 0:
        date_1 = datetime.datetime.strptime(value, "%m-%d-%y")
        end_date = date_1 + datetime.timedelta(days=(args+1)*7)
        date = end_date
    return date


@register.simple_tag(takes_context=True)
def usuarioNome(context):
    request = context['request']
    usuario = Usuario.objects.get( id=auth(request).id )
    return usuario.nome


@register.simple_tag(takes_context=True)
def usuarioNivel(context):
    request = context['request']
    usuario = Usuario.objects.get( id=auth(request).id )
    return usuario.grupo.acessos.split(';')


@register.simple_tag(takes_context=True)
def usuarioFoto(context):
    request = context['request']
    usuario = Usuario.objects.get( id=auth(request).id )
    return usuario.foto


@register.simple_tag(takes_context=True)
def usuarioSegmentos(context):
    request = context['request']
    usuario = Usuario.objects.get( id=auth(request).id )
    return usuario.segmentos.split(';')


@register.filter(name='usuarioSegmentoCheck')
def usuarioSegmentoCheck(value, args):
    check = False
    if value != None:
        usuario = Usuario.objects.get(id=value)
        check = args in usuario.segmentos.split(';')
    return check


@register.filter(name='filtroSegmentos')
def filtroSegmentos(value, args):
    segmentos = ''
    if args == 'segmentos':
        if len(value.split(';')) == 4:
            segmentos = 'Todos'
        else:
            segmentos = value.replace('_', ' ').replace(';', ', ').replace('e', 'é')
    if args == 'status':
        segmentos = 'Pendente'
        if value:
            segmentos = 'Ativo'

    return segmentos

@register.filter(name='usuarioSegmento')
def usuarioSegmento(value):
    result = None
    if value == 'infantil':
        result = settings.SEGMENTOS['infantil']
    if value == 'anos_iniciais':
        result = settings.SEGMENTOS['anos_iniciais']
    if value == 'anos_finais':
        result = settings.SEGMENTOS['anos_finais']
    if value == 'medio':
        result = settings.SEGMENTOS['medio']
    return result


@register.simple_tag(takes_context=True)
def planejamentoRespondido(context):
    request = context['request']
    respostas = GradePlanComment.objects.filter(planejamento__usuario__id=auth(request).id, visto=False)

    return respostas.count()


@register.filter(name='formatarData')
def formatarData(value, arg):
    data = None
    if arg == 'full':
        data = value.strftime('%d/%m/%Y %H:%M:%S')
    if arg == 'lapsed':
        data = datetime.datetime.strptime(value, '%d/%m/%y %H:%M:%S') - datetime.datetime.now()
    return data


@register.filter(name='indexTurma')
def indexTurma(value):
    if type(value) == 'str':
        value = int(value)
    return settings.TURMAS[value]


@register.filter(name='limitadorTexto')
def limitadorTexto(value, args):
    mensagem = value
    if len(mensagem) >= args:
        mensagem = mensagem[:(args-3)] + '...'
    return mensagem


@register.filter(name='soma')
def soma(value, args):
    return value + args

@register.filter(name='fileType')
def fileType(value):
    if 'http' in value:
        file = True
    else:
        file = value.split('/')[-1].split('.')[-1]
    return file == 'pdf' or file == True