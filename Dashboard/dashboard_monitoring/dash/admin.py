from django.contrib import admin
from .models import Categorie, Vulnerabilite, Actualite
from django.utils.text import Truncator

#configuration affichage model Vulnerabilite
class VulnerabiliteAdmin(admin.ModelAdmin):
    list_display = ('nom', 'source', 'date', 'apercu_contenu')
    prepopulated_fields = {'slug': ('nom',)}
    list_filter = ('source', 'categorie',)
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('nom', 'contenu')

    # Configuration du formulaire d'édition
    fieldsets = (
        # Fieldset 1 : meta-info (nom, source ...)
        ('Général',{
            'classes':['collapse', ],
            'fields': ('nom','slug','source', 'categorie'),
        }),
        # Fieldset 2 : contenu de l'article
        ('Contenu de la vulnerabilite',{
            'description': 'Le formulaire accepte les balises HTML. Utilisez-les à bon escient !',
            'fields':('contenu',)
        }),
    )

    # colonnes personnalisés
    def apercu_contenu(self, vulnerabilite):
        """ 
        Retourne les 40 premiers caractères du contenu de la vulnérabilité,
        suivi de points de suspension si le texte est plus long.
        """
        text = vulnerabilite.contenu[0:40]
        if len(vulnerabilite.contenu) > 40:
            return '%s...' % text
        else:
            return text
    
    # En-tête de notre colonne
    apercu_contenu.short_description = "Aperçu du contenu"

# configuration affichage model Actualite
class ActualiteAdmin(admin.ModelAdmin):
    list_display = ('titre','source','date', 'apercu_contenu')
    prepopulated_fields = {'slug': ('titre',)}
    list_filter = ('source', 'categorie',)
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('titre','contenu')

        # Configuration du formulaire d'édition
    fieldsets = (
        # Fieldset 1 : meta-info (nom, source ...)
        ('Général',{
            'classes':['collapse', ],
            'fields': ('titre','slug', 'source', 'categorie')
        }),
        # Fieldset 2 : contenu de l'article
        ('Contenu de la vulnerabilite',{
            'description': 'Le formulaire accepte les balises HTML. Utilisez-les à bon escient !',
            'fields':('contenu',)
        }),
    ) 
    def apercu_contenu(self, actualite):
        return Truncator(actualite.contenu).chars(40, truncate='...')

    # En-tête de notre colonne
    apercu_contenu.short_description = "Aperçu du contenu"

# Register your models here.
admin.site.register(Categorie)
admin.site.register(Vulnerabilite, VulnerabiliteAdmin)
admin.site.register(Actualite, ActualiteAdmin)
