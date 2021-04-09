from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Pessoa


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        labels = {
            'username': ('Email'),
        }
        widgets = {
            'username': forms.EmailInput(attrs = {'class':'form-control'}),
            'password1': forms.PasswordInput(attrs = {'class':'form-control'}),
            'password2': forms.PasswordInput(attrs = {'class':'form-control'}),
        }

class CreatePessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome','cep','endereco','numero','bairro','complemento','cidade','estado']

        widgets = {
            'nome': forms.TextInput(attrs = {'class':'form-control'}),
            'cep': forms.TextInput(attrs = {'class':'form-control'}),
            'endereco': forms.TextInput(attrs = {'class':'form-control'}),
            'numero': forms.NumberInput(attrs = {'class':'form-control'}),
            'bairro': forms.TextInput(attrs = {'class':'form-control'}),
            'complemento': forms.TextInput(attrs = {'class':'form-control'}),
            'cidade': forms.TextInput(attrs = {'class':'form-control'}),
            'estado': forms.TextInput(attrs = {'class':'form-control'}),
        }
