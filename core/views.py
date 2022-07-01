from dataclasses import dataclass
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import producto
from .forms import CustomUserForm, productoform
from django.contrib.auth import login, authenticate 
from django.contrib import messages
from cart.cart import Cart




from rest_framework import viewsets
from .serializer import ProductoSerializer

class ProductoViewset(viewsets.ModelViewSet):
    queryset = producto.objects.all()
    serializer_class = ProductoSerializer

# Create your views here.



def home(request):
    return render(request, 'core/home.html')

def quienes_somos(request):
    return render(request, 'core/quienes_somos.html')

def api(request):
    return render(request,'core/api.html')


def register(request):
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            return redirect(to='login')
    else:
        form=CustomUserForm()
    return render(request,'registration/register.html',{'form':form})

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

def listar(request):
    productos=producto.objects.all()
    data={'productos':productos}
    return render(request,'core/listar.html',data)


@login_required
def cartdetail(request):
    cart=Cart(request)
    return render(request,'core/cartdetail.html',{'cart':cart})

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

def convertidor(request):
    return render(request,'core/convertidor.html')

@permission_required('core.modificarprod')
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
@permission_required ('core.eliminarprod')
def eliminarprod(request,id):
    productos=producto.objects.get(id=id)
    productos.delete()
    return redirect(to='listar')




@login_required(login_url="registration/login/")
def cart_add(request, id):
    cart = Cart(request)
    producto = producto.objects.get(id=id)
    cart.add(producto=producto)
    return redirect("home")


@login_required(login_url="registration/login/")
def item_clear(request, id):
    cart = Cart(request)
    producto = producto.objects.get(id=id)
    cart.remove(producto)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    producto = producto.objects.get(id=id)
    cart.add(producto=producto)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    producto = producto.objects.get(id=id)
    cart.decrement(producto = producto)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'core/cartdetail.html')
