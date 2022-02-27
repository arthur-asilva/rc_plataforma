from django.urls import path
from . import views

urlpatterns = [
    path('contatos/', views.ContatosView, name='contatos_view'),
    path('notificacoes/', views.NotificacoesView, name='notificacoes_view'),
    path('contatos_request/', views.ContatosRequestView, name='contatos_request_view'),
]