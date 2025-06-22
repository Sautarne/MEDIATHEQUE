from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Media, Livre, Dvd, Cd, JeuDePlateau, Emprunteur

admin.site.register(Emprunteur)
admin.site.register(Media)
admin.site.register(Livre)
admin.site.register(Dvd)
admin.site.register(Cd)
admin.site.register(JeuDePlateau)