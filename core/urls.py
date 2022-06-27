from xml.etree.ElementInclude import include
from .views import home, listar,  quienes_somos, api, register, login, productos, comprar, creditodebito, agregarprod,listar, modificarprod, eliminarprod
from django.urls import path, include
from django.contrib import admin 


urlpatterns = [
    path('', home, name="home"),
    path('quienes-somos/',quienes_somos, name="quienes_somos" ),
    path('register/',register,name="register"),
    path('login/',login,name="login"),
    path('productos/', productos,name="productos"),
    path('api/',api, name="api"),
    path('comprar/',comprar, name="comprar"),
    path('creditodebito/',creditodebito, name="creditodebito"),
    path('agregarprod/',agregarprod, name="agregarprod"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('listar',listar,name="listar"),
    path('modificarprod/<id>',modificarprod, name="modificarprod"),
    path('eliminarprod/<id>',eliminarprod, name="eliminarprod"),
    ]

