from django.urls import path
from . import views

urlpatterns = [
    path('add_turma/', views.CadastroTurmaView, name='add_turma'),
    # path('add_courseware/', views.CoursewareView, name='add_courseware'),
]