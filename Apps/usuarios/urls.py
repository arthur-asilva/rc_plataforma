from django.urls import path
from . import views


urlpatterns = [
    path('', views.LoginView, name='login_view'),
    path('logout/', views.LogoutView, name='logout_view'),
    path('trocar_senha/', views.TrocarSenhaView, name='trocar_senha'),
    path('add_usuario/', views.CadastroProfessorView, name='add_usuario'),
]