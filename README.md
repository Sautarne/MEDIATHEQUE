# Système de Gestion de Médiathèque

## Description
Application web Django pour la gestion d'une médiathèque permettant de gérer les membres, les médias (livres, DVDs, CDs, jeux de plateau) et les emprunts.

## Prérequis
- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

## Installation

### 1. Cloner ou télécharger le projet
```bash
# Si depuis GitHub
git clone [URL_DU_REPO]
cd mediatheque

# Ou extraire l'archive ZIP dans un dossier
```

### 2. Créer un environnement virtuel
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Mac/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Installer Django
```bash
pip install django
```

### 4. Configurer la base de données
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Créer un compte administrateur
```bash
python manage.py createsuperuser
# Suivre les instructions (username, email, password)
```

### 6. Lancer le serveur
```bash
python manage.py runserver
```

## Utilisation

### Accès aux applications
- **Interface d'administration** : http://127.0.0.1:8000/admin/
- **Application bibliothécaire** : http://127.0.0.1:8000/bibliothecaire/membres/
- **Application consultation publique** : http://127.0.0.1:8000/consultation/

### Fonctionnalités principales

#### Application Bibliothécaire
- Créer un membre : `/bibliothecaire/membres/creer/`
- Liste des membres : `/bibliothecaire/membres/`
- Modifier un membre : Cliquer "Modifier" dans la liste
- Liste des médias : `/bibliothecaire/liste_medias/`
- Créer un emprunt : `/bibliothecaire/emprunt/creer/`
- Retourner un emprunt : `/bibliothecaire/emprunt/retour/`
- Ajouter un média : `/bibliothecaire/media/ajouter/`

#### Application Consultation
- Catalogue public : `/consultation/`

## Tests
Pour lancer les tests :
```bash
python manage.py test
```

## Données de test
Des données de test peuvent être créées via l'interface d'administration ou en utilisant les formulaires de l'application.

## Structure du projet
```
mediatheque/
├── manage.py
├── mediatheque/          # Configuration Django
├── bibliothecaire/       # App pour les bibliothécaires
│   ├── models.py        # Modèles (Media, Livre, Emprunteur...)
│   ├── views.py         # Vues (logique métier)
│   ├── forms.py         # Formulaires Django
│   ├── urls.py          # URLs de l'app
│   └── templates/       # Templates HTML
└── consultation/        # App pour la consultation publique
    ├── views.py
    ├── urls.py
    └── templates/
```

## Arrêter l'application
- Appuyer sur `Ctrl+C` dans le terminal pour arrêter le serveur
- Tapez `deactivate` pour sortir de l'environnement virtuel