from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth, messages
from .forms import CreateUserForm, CreatePessoaForm, CreateProdutoForm
from .decorators import inautentificado_user
from django.contrib.auth.decorators import login_required
from .models import Produto


def index(request):
    return render(request, 'index.html')

@login_required(login_url='login_page')
def home(request):
    data = {}
    data['produtos'] = Produto.objects.count()
    return render(request, 'home.html',data)

@login_required(login_url='index_page')
def deletar_produto(request, id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    return redirect('produto_page')

@inautentificado_user
def login(request):
    if request.user.is_authenticated:
	    return redirect('home_page')
	
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home_page')
        messages.info(request, 'Email ou senha incorretos')

    data = {}
    return render(request, 'login.html', data)

@inautentificado_user
def cadastro(request):
    
    if request.method == 'POST':
        form_user = CreateUserForm(request.POST)
        form_pessoa = CreatePessoaForm(request.POST)

        #Validando forms 
        if form_user.is_valid() and form_pessoa.is_valid():
            user = form_user.save()
            user.save()
            pessoa = form_pessoa.save(commit = False)
            pessoa.user = user
            pessoa.save()

            return redirect('login_page')
        #Se o form nao passou apresente erro
        messages.info(request, 'Formulário preenchido incorretamente')
        return redirect('cadastro_page')
   
    form_user = CreateUserForm()
    form_pessoa = CreatePessoaForm()
    
    data = {}
    data['form_user'] = form_user
    data['form_pessoa'] = form_pessoa
    return render(request, 'cadastro.html', data)

@login_required(login_url='index_page')
def produto(request):
    if request.method == 'POST':
        form = CreateProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('produto_page')
    data = {}
    data['produtos'] = Produto.objects.all()
    data['produto_form'] = CreateProdutoForm()
    return render(request, 'produto.html', data)


def logout(request):
    auth.logout(request)
    return redirect('index_page')