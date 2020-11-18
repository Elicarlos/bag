from django.db import models

# Create your models here.

class Tamanho(models.Model):
    tamanho = models.CharField(max_length=30)
    
    def __str__(self):
        return self.tamanho


class Categoria(models.Model):
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.categoria


class Produto(models.Model):
    descricao = models.CharField(max_length=50)
    preco = models.FloatField()
    estoque = models.IntegerField()
    foto = models.ImageField(upload_to='produtos')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    tamanho = models.ForeignKey(Tamanho, on_delete=models.CASCADE)
    genero = models.CharField(max_length=30)
    ativo = models.BooleanField(default=True)


class Cliente(models.Model):
    cpf = models.CharField(max_length=30)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nome)

    class Meta:
        db_table = 'cliente'




class Pedido(models.Model):  
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedido')
    itens = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='pedido')
    data = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2) 
          

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'pedido'






