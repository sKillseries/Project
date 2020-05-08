from django.urls import path

from . import views

urlpatterns = [
    path('accueil', views.home, name='accueil'),
    path('cybersecurity', views.view_cybersecurity, name='cybersecurity'),
    path('vulnerabilite/<int:id>-<slug:slug>$', views.consultation, name='consultation'),
    path('actualite/<int:id>-<slug:slug>$', views.lire, name='lire'),
]