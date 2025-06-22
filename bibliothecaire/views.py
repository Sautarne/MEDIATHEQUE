from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Emprunteur, Media, Livre, Dvd, Cd, JeuDePlateau
from .forms import EmprunteurForm, EmpruntForm, RetourForm, MediaForm


def liste_membres(request):
    membres = Emprunteur.objects.all()
    return render(request, 'bibliothecaire/liste_membres.html', {'membres': membres})


def creer_membre(request):
    if request.method == 'POST':
        form = EmprunteurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_membres')
    else:
        form = EmprunteurForm()

    return render(request, 'bibliothecaire/creer_membre.html', {'form': form})

def liste_medias(request):
    medias = Media.objects.all()
    return render(request, 'bibliothecaire/liste_medias.html', {'medias': medias})


def creer_emprunt(request):
    if request.method == 'POST':
        form = EmpruntForm(request.POST)
        if form.is_valid():
            media = form.cleaned_data['media']
            emprunteur = form.cleaned_data['emprunteur']

            media.disponible = False
            media.dateEmprunt = timezone.now().date()
            media.emprunteur = emprunteur
            media.save()

            return redirect('liste_medias')
    else:
        form = EmpruntForm()

    return render(request, 'bibliothecaire/creer_emprunt.html', {'form': form})


def retour_emprunt(request):
    if request.method == 'POST':
        form = RetourForm(request.POST)
        if form.is_valid():
            media = form.cleaned_data['media']

            media.disponible = True
            media.dateEmprunt = None
            media.emprunteur = None
            media.save()

            return redirect('liste_medias')
    else:
        form = RetourForm()

    return render(request, 'bibliothecaire/retour_emprunt.html', {'form': form})


def ajouter_media(request):
    if request.method == 'POST':
        form = MediaForm(request.POST)
        if form.is_valid():
            type_media = form.cleaned_data['type_media']
            name = form.cleaned_data['name']
            createur = form.cleaned_data['createur']

            if type_media == 'livre':
                media = Livre(name=name, createur=createur)
            elif type_media == 'dvd':
                media = Dvd(name=name, createur=createur)
            elif type_media == 'cd':
                media = Cd(name=name, createur=createur)
            elif type_media == 'jeu':
                media = JeuDePlateau(name=name, createur=createur)

            media.save()
            return redirect('liste_medias')
    else:
        form = MediaForm()

    return render(request, 'bibliothecaire/ajouter_media.html', {'form': form})


def modifier_membre(request, membre_id):
    membre = get_object_or_404(Emprunteur, id=membre_id)

    if request.method == 'POST':
        form = EmprunteurForm(request.POST, instance=membre)
        if form.is_valid():
            form.save()
            return redirect('liste_membres')
    else:
        form = EmprunteurForm(instance=membre)

    return render(request, 'bibliothecaire/modifier_membre.html', {'form': form, 'membre': membre})