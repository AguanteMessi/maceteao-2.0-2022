from dataclasses import dataclass
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from core.forms import CustomUserCreationForm
from .models import producto
from .forms import productoform

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def quienes_somos(request):
    return render(request, 'core/quienes_somos.html')

def api(request):
    return render(request,'core/api.html')

def register(request):
    data = {
        'form':CustomUserCreationForm()
    }
    return render(request,'registration/register.html', data) 

def login(request):
    return render(request,'core/login.html')

def productos(request):
    productos= producto.objects.all()
    data={'productos':productos}
    return render(request,'core/productos.html',data)

def comprar(request):
    return render(request,'core/comprar.html')

def creditodebito(request):
    return render(request,'core/creditodebito.html')

@login_required

def agregarprod(request):
<<<<<<< HEAD
    data={
        'form':productoform()
        }
    return render(request,'core/agregarprod.html',data)


def listar(request):
    return render(request,'core/listar.html')
=======

    return render(request,'core/agregarprod.html')
>>>>>>> origin/pedro



