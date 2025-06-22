from django.db import models

class Emprunteur(models.Model):
    name = models.CharField(max_length=200)
    bloque = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Media(models.Model):
    name = models.CharField(max_length=200)
    createur = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)
    dateEmprunt = models.DateField(null=True, blank=True)
    emprunteur = models.ForeignKey(Emprunteur, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Livre(Media):
    pass

class Dvd(Media):
    pass

class Cd(Media):
    pass

class JeuDePlateau(Media):
    pass