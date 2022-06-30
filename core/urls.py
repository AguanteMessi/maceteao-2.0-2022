
from django.db import router
from .views import cart_add, cart_clear, cartdetail, eliminarprod, home, item_clear, item_decrement, item_increment, listar, modificarprod, quienes_somos,register, login, productos, comprar, creditodebito, convertidor, agregarprod,listar, api
from django.urls import path
from django.urls.conf import include
from django.contrib import admin 
from .views import ProductoViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Productos', ProductoViewset)


urlpatterns = [
    path('', home, name="home"),
    path('quienes-somos/',quienes_somos, name="quienes_somos" ),
    path('register/',register,name="register"),
    path('login/',login,name="login"),
    path('productos/', productos,name="productos"),
    path('comprar/',comprar, name="comprar"),
    path('creditodebito/',creditodebito, name="creditodebito"),
    path('agregarprod/',agregarprod, name="agregarprod"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('listar',listar,name="listar"),
    path('api/', include(router.urls)),
    path('convertidor/',convertidor,name="convertidor"),
    path('modificarprod/<id>',modificarprod, name="modificarprod"),
    path('eliminarprod/<id>',eliminarprod, name="eliminarprod"),
    path('cart/add/<int:id>/', cart_add , name='cart_add'),
    path('cart/item_clear/<int:id>/', item_clear , name='item_clear'),
    path('cart/item_increment/<int:id>/', item_increment , name='item_increment'),
    path('cart/item_decrement/<int:id>/', item_decrement , name='item_decrement'),
    path('cart/cart_clear/', cart_clear , name='cart_clear'),
    path('cart/cartdetail/', cartdetail ,name='cartdetail'),
    ]


