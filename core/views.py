from dataclasses import dataclass
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import producto
from .forms import CustomUserForm, productoform
from django.contrib.auth import login, authenticate 
from django.contrib import messages


# Create your views here.



def home(request):
    return render(request, 'core/home.html')

def quienes_somos(request):
    return render(request, 'core/quienes_somos.html')

def api(request):
    return render(request,'core/api.html')


def register(request):
    data = {
        'form':CustomUserForm()
    }
    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save();
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate (username=username, password=password)
            login(request, user)
            return redirect(to='home')

    return render(request, "registration/register.html", data)

def login(request):
    return render(request,'registration/login.html')

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

    return render(request,'core/agregarprod.html')
    data={
        'form':productoform()
        }
    return render(request,'core/agregarprod.html',data)


def listar(request):
    return render(request,'core/listar.html')



