from django.shortcuts import render
from bibliothecaire.models import Media

def liste_medias_consultation(request):
    medias = Media.objects.all()
    return render(request, 'consultation/liste_medias.html', {'medias': medias})