from django.shortcuts import render
from Apps.usuarios.views import auth
from Apps.usuarios.models import Usuario
from .models import Chat
from Apps.tools.views import decode, encode
from django.http import JsonResponse
from django.db.models import Q


def ContatosView(request):
    usuario = auth(request)
    data = {
        'usuario': usuario,
        'adms': Usuario.objects.filter(~Q(id=usuario.id), grupo__nome='administrador'),
        'professores': Usuario.objects.filter(~Q(id=usuario.id), grupo__nome='professor'),
        'conversa': request.GET.get('c', 0)
    }
    return render(request, 'contatos/contatos.html', data)



def ContatosRequestView(request):
    
    if request.method == 'POST':
        chat = Chat()
        usuario = auth(request)
        chat.de_usuario = usuario
        chat.para_usuario = Usuario.objects.get(id=decode(request.POST['user']))

        if request.GET.get('old_m', None) != None:
                query = Chat.objects.values('id', 'data', 'data_str', 'mensagem', 'de_usuario__nome', 'de_usuario__foto', 'visto').filter(Q(para_usuario__id=chat.para_usuario.id) | Q(de_usuario__id=chat.para_usuario.id)).order_by('id')
                return JsonResponse({'mensagens': list(query)})

        if request.POST.get('up', None) != None:
            Chat.objects.filter(Q(para_usuario__id=usuario.id), visto=False).update(visto=True)
            return JsonResponse({'status': '200'})

        if request.POST.get('message', None) != None:
            chat.mensagem = request.POST['message']
            chat.save()
            query = Chat.objects.values('id', 'data', 'data_str', 'mensagem', 'de_usuario__nome', 'de_usuario__foto', 'visto').filter(Q(para_usuario__id=chat.para_usuario.id) | Q(de_usuario__id=chat.para_usuario.id)).order_by('id')
            return JsonResponse({'mensagens': list(query) })

        if request.GET.get('r', None) != None:
            query = Chat.objects.values('id', 'data', 'data_str', 'mensagem', 'de_usuario__nome', 'de_usuario__foto', 'visto').filter(Q(id__gt=int(request.POST['m_id'])), Q(para_usuario__id=chat.para_usuario.id) | Q(de_usuario__id=chat.para_usuario.id)).order_by('id')
            return JsonResponse({'mensagens': list(query)})



def NotificacoesView(request):
    chat = Chat.objects.values('de_usuario__id', 'id', 'data_str', 'mensagem', 'de_usuario__nome', 'de_usuario__foto').filter(para_usuario__id=auth(request).id, visto=False).order_by('-id')[:5]
    return JsonResponse({'mensagens': list(chat)})