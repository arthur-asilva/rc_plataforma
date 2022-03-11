from django.shortcuts import render, redirect
from .models import Grupo, Usuario
from Apps.turmas.models import Turma
from Apps.tools.views import encode, decode, uploadArquivo, AuthValidation
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import random, string

@AuthValidation
def LoginView(request):

    usuario = None

    if request.method == 'POST':
        usuario = Usuario.objects.filter(email=request.POST['email'], senha=request.POST['senha'], status=True)
        if usuario.count() > 0:
            request.session['auth_session'] = encode(usuario[0].id)
            return redirect('dash/')

    if request.GET.get('conf', None) != None and request.GET.get('u', None) != None:
        usuario = Usuario.objects.get(id=int(decode(request.GET['u'])))
        usuario.status = True
        usuario.save()

    return render(request, 'login.html')


def send_html_email(to_list, subject, template_name, context, sender='coordenacao@robociencia.com.br'):
    msg_html = render_to_string(template_name, context)
    msg = EmailMessage(subject=subject, body=msg_html, from_email=sender, bcc=[to_list,])
    msg.content_subtype = "html"  # Main content is now text/html
    return msg.send()


def auth(request):
    id = int(decode(request.session['auth_session']))
    usuario = Usuario.objects.get(id=id)
    return usuario


def LogoutView(request):
    request.session.modified = True
    del request.session['auth_session']
    return redirect('/')


@AuthValidation
def TrocarSenhaView(request):
    foto = request.FILES.get('anexo', None)
    turmas = Turma.objects.values('escola__unidade__cidade', 'escola__unidade__estado').filter(professor=auth(request)).distinct()

    if request.method == 'POST':
        usuario = Usuario.objects.get(id=auth(request).id)
        if foto != None:
            usuario.foto = uploadArquivo(foto, 'Usuarios/' + str(usuario.id) + '/foto_perfil')
        if request.POST['senha_atual'] == auth(request).senha:
            usuario.senha = request.POST['senha_nova']
            usuario.save()
        
        usuario.save()
        return redirect('../logout/')
        
    data = {
        'usuario': auth(request),
        'turmas': turmas
    }
    return render(request, 'usuarios/trocar_senha.html', data)



@AuthValidation
def CadastroProfessorView(request):

    editar = request.GET.get('id', None)
    usuario = Usuario()

    if editar != None:
        editar = Usuario.objects.get(id=editar)
        usuario = editar

    if request.method == 'POST':
        senha = password_generate(4,4)
        usuario.nome = request.POST['nome']
        usuario.grupo = Grupo.objects.get(id=request.POST['grupo'])
        usuario.email = request.POST['email']
        usuario.senha = senha
        usuario.telefone = request.POST['telefone']
        usuario.segmentos = ';'.join(request.POST.getlist('segmentos'))
        usuario.status = request.POST['status']
        usuario.save()

        context = {
            'nome': usuario.nome.split(' ')[0], 
            'grupo': usuario.grupo.nome, 
            'id': encode(usuario.id),
            'senha': senha
        }

        send_html_email(request.POST['email'], 'Confirmação de cadastro Robô Ciência', 'usuarios/email_confirmacao.html', context, "Dont Reply <coordenacao@robociencia.com.br>")
            
        return redirect('../add_usuario/')

    data = {
        'grupos': Grupo.objects.all(),
        'usuarios': Usuario.objects.all(),
        'editar': editar
    }
    return render(request, 'usuarios/cadastro.html', data)



def password_generate(letter_count, digit_count):
    str1 = ''.join((random.choice(string.ascii_letters) for x in range(letter_count)))  
    str1 += ''.join((random.choice(string.digits) for x in range(digit_count)))  
    sam_list = list(str1)
    random.shuffle(sam_list)
    final_string = ''.join(sam_list)

    return final_string