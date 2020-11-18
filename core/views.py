from django.shortcuts import render
from . models import Produto

# Create your views here.

def list_all_produtos(request):
    prod = Produto.objects.filter(ativo=True)
    print(prod.query)
    return render(request, 'list-produtos.html', {'prod': prod})

