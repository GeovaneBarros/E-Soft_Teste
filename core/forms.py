from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Pessoa, Produto


class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        

class CreatePessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome','cep','endereco','numero','bairro','complemento','cidade','estado']

        widgets = {
            'nome': forms.TextInput(attrs = {'class':'form-control'}),
            'cep': forms.TextInput(attrs = {'class':'form-control', 'id':'cep', 'onblur':"pesquisacep(this.value);"}),
            'endereco': forms.TextInput(attrs = {'class':'form-control', 'id':'endereco'}),
            'numero': forms.NumberInput(attrs = {'class':'form-control'}),
            'bairro': forms.TextInput(attrs = {'class':'form-control', 'id':'bairro'}),
            'complemento': forms.TextInput(attrs = {'class':'form-control'}),
            'cidade': forms.TextInput(attrs = {'class':'form-control', 'id':'cidade'}),
            'estado': forms.TextInput(attrs = {'class':'form-control','id':'estado'}),
        }
class CreateProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque']

        widgets={
            'nome': forms.TextInput(attrs = {'class':'form-control', 'id':'nome_produto'}),
            'preco': forms.NumberInput(attrs = {'class':'form-control'}),
            'estoque': forms.NumberInput(attrs = {'class':'form-control'}),
        }