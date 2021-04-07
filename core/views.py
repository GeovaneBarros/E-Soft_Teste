from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def produto(request):
    return render(request, 'produto.html')