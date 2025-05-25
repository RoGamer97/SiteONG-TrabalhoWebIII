from django import forms

from django import forms
from django.core.exceptions import ValidationError
import re

def clean_nome(self):
    nome = self.cleaned_data['nome'].strip()

    if len(nome) < 3:

        raise ValidationError(" O nome não existe")
    
    if len(nome.plit()) < 2:
        
        raise ValidationError("Digite seu nome completo")
    
    if not re.match(r'^[A-Za-zÀ-ÿ ]+$', nome):

        raise ValidationError("Use apenas letras no nome")
    
    return nome
    
def clean_idade(self):
    idade = self.cleaned_data['idade']
    if idade < 18:
    
        raise ValidationError("Você precisa ter pelo menos 18 anos para se voluntariar.")
        
    return idade

def clean_telefone(self):
    telefone = self.cleaned_data['telefone'].strip()

    telefone_numerico = re.sub(r'\D', '', telefone)

    if len(telefone_numerico) not in [10,11]:

        raise ValidationError("Inforeme um telefone válido com DDD e número")
    
    return telefone



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

    
