from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=254)
    preco = models.FloatField()
    estoque = models.IntegerField()

    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    nome = models.CharField(max_length=62)
    endereco = models.CharField(max_length=254)
    numero = models.CharField(max_length=8)
    complemento = models.CharField(max_length=254, blank=True, null = False)
    bairro = models.CharField(max_length=64)
    cep = models.CharField(max_length=8)
    cidade = models.CharField(max_length=64)
    estado = models.CharField(max_length=32)
    def __str__(self):
        return self.nome