from django.urls import path
from . import views

urlpatterns = [
    path('gradeplans/', views.GradePlansView, name='grade_plans_view'),
    path('viewplan/', views.VisualizarView, name='read_plan_view'),
    path('newplan/', views.NovoPlanejamentoView, name='new_plan_view'),
    path('responder_planejamento/', views.PlanejamentoRespostaView, name='responder_planejamento_view'),
]