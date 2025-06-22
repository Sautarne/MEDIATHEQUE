from django import forms
from .models import Emprunteur, Media

class EmprunteurForm(forms.ModelForm):
    class Meta:
        model = Emprunteur
        fields = ['name', 'bloque']

class EmpruntForm(forms.Form):
    media = forms.ModelChoiceField(
        queryset=Media.objects.filter(disponible=True),
        label="Média à emprunter"
    )

    emprunteur = forms.ModelChoiceField(
        queryset=Emprunteur.objects.filter(bloque=False),
        label="Emprunteur"
    )

class RetourForm(forms.Form):
    media = forms.ModelChoiceField(
        queryset=Media.objects.filter(disponible=False),
        label="Média à retourner"
    )


class MediaForm(forms.Form):
    TYPE_CHOICES = [
        ('livre', 'Livre'),
        ('dvd', 'DVD'),
        ('cd', 'CD'),
        ('jeu', 'Jeu de plateau'),
    ]

    type_media = forms.ChoiceField(choices=TYPE_CHOICES, label="Type de média")
    name = forms.CharField(max_length=200, label="Nom")
    createur = forms.CharField(max_length=100, label="Créateur")