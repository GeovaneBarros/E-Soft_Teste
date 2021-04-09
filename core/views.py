from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from .forms import CreateUserForm, CreatePessoaForm
from .decorators import inautentificado_user
from django.contrib.auth.decorators import login_required
from .models import Produto
# Create your views here.


def index(request):
    return render(request, 'index.html')

@login_required(login_url='index_page')
def home(request):
    return render(request, 'home.html')

@inautentificado_user
def login(request):
    if request.user.is_authenticated:
	    return redirect('home_page')
	
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home_page')
        messages.info(request, 'Email ou senha incorretos')

    context = {}
    return render(request, 'login.html', context)

@inautentificado_user
def cadastro(request):
    

    if request.method == 'POST':
        #Resgatando os formularios
        form_user = CreateUserForm(request.POST)
        form_pessoa = CreatePessoaForm(request.POST)

        #Validando forms 
        if form_user.is_valid() and form_pessoa.is_valid():
            user = form_user.save()
            user.set_password(user.password)  
            user.save()
            pessoa = form_pessoa.save(commit = False)
            pessoa.user = user
            pessoa.save()
            return redirect('index_page')
    
    #Criando Formularios
    form_user = CreateUserForm()
    form_pessoa = CreatePessoaForm()
    
    data = {}
    data['form_user'] = form_user
    data['form_pessoa'] = form_pessoa
    return render(request, 'cadastro.html', data)

@login_required(login_url='index_page')
def produto(request):
    data = {}
    data['produtos'] = Produto.objects.all()
    return render(request, 'produto.html', data)


def logout(request):
    auth.logout(request)
    return redirect('index_page')