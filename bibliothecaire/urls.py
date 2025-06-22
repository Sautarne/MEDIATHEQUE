from django.urls import path
from . import views

urlpatterns = [
    path('membres/', views.liste_membres, name='liste_membres'),
    path('membres/creer/', views.creer_membre, name='creer_membre'),
    path('liste_medias/', views.liste_medias, name='liste_medias'),
    path('emprunt/creer/', views.creer_emprunt, name='creer_emprunt'),
    path('emprunt/retour/', views.retour_emprunt, name='retour_emprunt'),
    path('media/ajouter/', views.ajouter_media, name='ajouter_media'),
    path('membres/modifier/<int:membre_id>/', views.modifier_membre, name='modifier_membre'),
]