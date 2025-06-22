from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from .models import Emprunteur, Livre, Media
from bibliothecaire.models import Livre


class EmprunteurTestCase(TestCase):
    def test_creation_emprunteur(self):
        """Test de création d'un emprunteur"""
        emprunteur = Emprunteur.objects.create(name="Test User", bloque=False)
        self.assertEqual(emprunteur.name, "Test User")
        self.assertFalse(emprunteur.bloque)


class VuesTestCase(TestCase):
    def setUp(self):
        """Données de test créées avant chaque test"""
        self.client = Client()
        self.emprunteur = Emprunteur.objects.create(name="Test User", bloque=False)
        self.livre = Livre.objects.create(name="Test Book", createur="Test Author")

    def test_liste_membres(self):
        """Test de la vue liste des membres"""
        response = self.client.get(reverse('liste_membres'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test User")

    def test_liste_medias(self):
        """Test de la vue liste des médias"""
        response = self.client.get(reverse('liste_medias'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Book")


class EmpruntTestCase(TestCase):
    def setUp(self):
        self.emprunteur = Emprunteur.objects.create(name="Test User", bloque=False)
        self.livre = Livre.objects.create(name="Test Book", createur="Test Author")

    def test_emprunt_logique(self):
        """Test de la logique d'emprunt"""
        self.assertTrue(self.livre.disponible)

        self.livre.disponible = False
        self.livre.dateEmprunt = timezone.now().date()
        self.livre.emprunteur = self.emprunteur
        self.livre.save()

        # Vérifications
        self.assertFalse(self.livre.disponible)
        self.assertEqual(self.livre.emprunteur, self.emprunteur)
        self.assertIsNotNone(self.livre.dateEmprunt)


class ConsultationTestCase(TestCase):
    def setUp(self):
        """Données de test"""
        self.client = Client()
        self.livre = Livre.objects.create(name="Test Book Public", createur="Test Author")

    def test_consultation_medias(self):
        """Test de la vue consultation publique"""
        response = self.client.get(reverse('consultation_medias'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Book Public")
        self.assertContains(response, "Catalogue de la médiathèque")