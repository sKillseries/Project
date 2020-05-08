from django import forms
from .models import Vulnerabilite, Actualite

class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    expediteur = forms.EmailField(label="Votre adresse mail")
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.",required=False)

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        sujet = cleaned_data.get('sujet')
        message = cleaned_data.get('message')

        return cleaned_data

class VulnerabiliteForm(forms.ModelForm):
    class Meta:
        model = Vulnerabilite
        fields = '__all__'

class ActualiteForm(forms.ModelForm):
    class Meta:
        model = Actualite
        fields = '__all__'
