import glob

from cryptography.fernet import Fernet
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import glob, os

from django.shortcuts import redirect

from Apps.usuarios.models import Usuario


def encode(mensagem):
    fernet = Fernet(settings.CHAVE)
    if(type(mensagem) != 'str'):
        mensagem = str(mensagem)
    encMessage = fernet.encrypt(mensagem.encode())
    encMessage = encMessage.decode("utf-8")
    return encMessage


def decode(mensagem):
    fernet = Fernet(settings.CHAVE)
    mensagem = mensagem.encode("utf-8")
    decMessage = fernet.decrypt(mensagem).decode()
    return decMessage


def uploadArquivo(arquivo, url):
    upload = arquivo
    fss = FileSystemStorage()

    for arquivo in glob.glob('media/' + url + '*'):
        os.remove(arquivo)

    url = url + '.' + upload.name.split('.')[-1]
    file = fss.save(url, upload)
    anexo = fss.url(file)

    return anexo


def gradePlanUpload(document, url):
    upload = document
    fss = FileSystemStorage()
    url = url + '.' + upload.name.split('.')[-1]
    file = fss.save(url, upload)
    file_path = fss.url(file)
    return file_path


def AuthValidation(func):
    def wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        permissao = False
        if func.__name__ != 'LoginView' and func.__name__ != 'DashView':
            usuario = Usuario.objects.get(id=decode(args[0].session['auth_session']))
            for acesso in usuario.grupo.acessos.split(';'):
                if acesso in func.__name__:
                    permissao = True
            if not permissao:
                    return redirect('../dash/')
        return result
    return wrap