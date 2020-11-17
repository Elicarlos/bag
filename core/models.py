from django.db import models

# Create your models here.

class Tamanho(models.Model):
    tamanho = models.CharField(max_length=30)

class Categoria(models.Model):
    categoria = models.CharField(max_length=50)

class Produto(models.Model):
    descricao = models.CharField(max_length=50)
    preco = models.DecimalField()
    estoque = models.IntegerField()
    foto = models.ImageField(upload_to='produtos')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    tamanho = models.ForeignKey(Tamanho, on_delete=models.CASCADE)
    genero = models.CharField(max_length=30)
    ativo = models.BooleanField(default=True)


class Cliente():
    cpf = models.CharField(max_length=30)
    nome = models.CharField(models.Model)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)




