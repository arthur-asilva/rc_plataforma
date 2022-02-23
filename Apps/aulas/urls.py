from django.urls import path
from . import views

urlpatterns = [
    path('planejamentos/', views.PlanejamentosView, name='planejamentos_view'),
    path('visualizar/', views.VisualizarView, name='visualizar_view'),
    path('enviados/', views.EnviadosView, name='enviados_view'),
    path('novo_planejamento/', views.NovoPlanejamentoView, name='novo_planejamento_view'),
    path('responder_planejamento/', views.PlanejamentoRespostaView, name='responder_planejamento_view'),
]