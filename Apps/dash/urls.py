from django.urls import path
from . import views

urlpatterns = [
    path('dash/', views.DashView, name='dash_view'),
]