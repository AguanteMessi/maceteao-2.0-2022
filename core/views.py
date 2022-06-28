from dataclasses import dataclass
<<<<<<< HEAD
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from core.forms import CustomUserCreationForm
=======
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
>>>>>>> origin/pedro
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

<<<<<<< HEAD
def listar(request):
    productos=producto.objects.all()
    data={'productos':productos}
    return render(request,'core/listar.html',data)


@login_required

@permission_required('core.add_producto')
def agregarprod(request):
    data={'form':productoform()}
    if request.method=='POST':
        form=productoform(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            data['mensaje']='Producto agregado correctamente'
        else :
            data['mensaje']='Error al agregar el producto'
    return render(request,'core/agregarprod.html',data)


=======

@login_required
def agregarprod(request):

    return render(request,'core/agregarprod.html')
    data={
        'form':productoform()
        }
    return render(request,'core/agregarprod.html',data)


def listar(request):
    return render(request,'core/listar.html')

>>>>>>> origin/pedro

def modificarprod(request,id):
    productos=producto.objects.get(id=id)
    data={'form':productoform(instance=productos)}
    if request.method=='POST':
        form=productoform(data=request.POST,instance=productos,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to='listar')
        data['form']=form
    return render(request,'core/modificarprod.html',data)

def eliminarprod(request,id):
    productos=producto.objects.get(id=id)
    productos.delete()
    return redirect(to='listar')
