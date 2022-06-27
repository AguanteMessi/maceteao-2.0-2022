from dataclasses import dataclass
from django.shortcuts import redirect, render
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

def listar(request):
    productos=producto.objects.all()
    data={'productos':productos}
    return render(request,'core/listar.html',data)


@login_required

def agregarprod(request):
    data={'form':productoform()}
    if request.method=='POST':
        form=productoform(request.POST)
        if form.is_valid():
            form.save()
            data['mensaje']='Producto agregado correctamente'
    return render(request,'core/agregarprod.html',data)



def modificarprod(request,id):
    productos=producto.objects.get(id=id)
    data={'form':productoform(instance=productos)}
    if request.method=='POST':
        form=productoform(data=request.POST,instance=productos)
        if form.is_valid():
            form.save()
            data['mensaje']='Producto modificado correctamente'
            data['form']=form
    return render(request,'core/modificarprod.html',data)

def eliminarprod(request,id):
    productos=producto.objects.get(id=id)
    producto.delete()
    return redirect('listar')
