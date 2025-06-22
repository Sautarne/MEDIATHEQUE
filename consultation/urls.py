from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_medias_consultation, name='consultation_medias'),
]