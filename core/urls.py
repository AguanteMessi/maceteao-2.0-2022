from xml.etree.ElementInclude import include
from .views import convertidor, home, listar,  quienes_somos, convertidor, register, login, productos, comprar, creditodebito, agregarprod,listar, modificarprod, eliminarprod
from django.urls import path, include
from django.contrib import admin 
from os import name
from django.db import router
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
    path('modificarprod/<id>',modificarprod, name="modificarprod"),
    path('eliminarprod/<id>',eliminarprod, name="eliminarprod"),
    path('api/', include(router.urls)),
    path('convertidor/',convertidor,name="convertidor"),
    ]

