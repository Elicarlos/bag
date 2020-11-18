from django.contrib import admin
from .models import Cliente, Categoria, Produto, Pedido, Tamanho

admin.site.register(Pedido)


# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['cpf', 'nome']


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['categoria']

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['descricao']




@admin.register(Tamanho)
class TamanhoAdmin(admin.ModelAdmin):
    list_display = ['tamanho']
