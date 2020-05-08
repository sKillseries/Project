from django.http import Http404
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from dash.models import Vulnerabilite
from dash.models import Actualite
from .forms import ContactForm, ActualiteForm, VulnerabiliteForm

# Create your views here.
def home(request):
    return render(request, 'dash/index.html')

def view_cybersecurity(request):
    """
    Vue du dashboard cybersecurity
    """
    vulnerabilites = Vulnerabilite.objects.all()
    actualites = Actualite.objects.all()

    return render(request, 'dash/cybersecurity.html', {'date': datetime.now(), 'dernieres_vulnerabilites': vulnerabilites, 'dernieres_actualites': actualites})

def consultation(request, id, slug):
    """ Affiche le contenu complet d'une vulnérabilité """
    vulnerabilite = get_object_or_404(Vulnerabilite, id=id, slug=slug)
    return render(request, 'dash/consultation.html', {'vulnerabilite': vulnerabilite})

def lire(request, id):
    """ Affiche le contenu complet d'un article """
    actualite = get_object_or_404(Actualite, id=id, slug=slug)
    return render(request, 'dash/lire.html', {'actualite':actualite})

