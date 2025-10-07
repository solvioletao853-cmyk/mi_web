from django.shortcuts import render
from .models import Cliente

# Create your views here.


def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})
