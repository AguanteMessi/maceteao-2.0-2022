from xml.etree.ElementInclude import include
from .views import home,  quienes_somos, api, register, login, productos, comprar, creditodebito, agregarprod
from django.urls import path, include
from django.contrib import admin 


urlpatterns = [
    path('admin/', admin.site.urls), 
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
    ]

admin.site.site_header = "Administrador de Maceteao"