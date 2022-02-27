from django.shortcuts import render
from cryptography.fernet import Fernet
from django.conf import settings
from Apps.tools.views import AuthValidation, encode
from Apps.usuarios.views import auth, send_html_email



@AuthValidation
def DashView(request):

    return render(request, 'dash/dash.html')
