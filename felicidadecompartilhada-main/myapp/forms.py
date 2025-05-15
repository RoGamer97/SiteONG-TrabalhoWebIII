from django import forms

from django import forms
from django.core.exceptions import ValidationError

class ContatoForm(forms.Form):
    nome = forms.CharField(
        max_length=100, 
        required=True, 
        widget=forms.TextInput(attrs={'id': 'nome'})
    )
    email = forms.EmailField(
        required=True, 
        widget=forms.EmailInput(attrs={'id': 'email'})
    )
    idade = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={'id': 'idade'})
    )
    telefone = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={'id': 'telefone'})
    )

    def clean_idade(self):
        idade = self.cleaned_data['idade']
        if idade < 18:
            raise ValidationError("Você precisa ter pelo menos 18 anos para se voluntariar.")
        return idade
