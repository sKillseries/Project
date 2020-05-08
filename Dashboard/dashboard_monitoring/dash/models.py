from django.db import models
from django.utils import timezone

# Create your models here.

# onglet vulnerabilité
class Vulnerabilite(models.Model):
    nom = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    source = models.CharField(max_length=100)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now, verbose_name="Date de parution")

    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "vulnerabilite"
        ordering = ['date']

    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaitre facilement les différents objets que
        nous traiterons plus tard dans l'administration
        """
        return self.nom

# onglet actualité
class Actualite(models.Model):
    titre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    source = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now, verbose_name="Date de parution")

    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "actualite"
        ordering = ['date']

    def __str__(self):
        return self.titre

# onglet affichant les tweet
class Twitter(models.Model):
    auteur = models.CharField(max_length=100)
    contenu = models.TextField(max_length=280)
    date = models.DateTimeField(default=timezone.now, verbose_name="Date de parution")

    class Meta:
        verbose_name = "twitter"
        ordering = ['date']

#création des catégories
class Categorie(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom