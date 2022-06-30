
from django.db import router
from .views import eliminarprod, home, listar, modificarprod, quienes_somos,register, login, productos, comprar, creditodebito, convertidor, agregarprod,listar
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
    ]

