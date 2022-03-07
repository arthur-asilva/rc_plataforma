from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from Apps.dash.views import DashView


urlpatterns = [
    path('tutoriais/', views.TutoriaisView, name='tutoriais_view'),
    path('complemento_tutoriais/', views.TutoriaisComplementoView, name='complemento_tutoriais'),
    path('add_complemento_tutoriais/', DashView, name='add_complemento_tutoriais'),
    path('cadastro_tutoriais/', views.TutoriaisCadastroView, name='cadastro_tutoriais'),
    path('apagar_tutoriais/', views.TutoriaisDeleteView, name='apagar_tutoriais'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)