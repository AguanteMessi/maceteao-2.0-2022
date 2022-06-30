from django import forms
from django.forms import ModelForm
from.models import *
from django.forms import fields
from .models import producto
import datetime 
from django.contrib.auth.forms import UserCreationForm

class productoform(ModelForm):
    nombre = forms.CharField(min_length=2, max_length=200)
    descripcion = forms.CharField(min_length=20, max_length=300)

    class Meta:
        model= producto
        fields=['nombre','precio','descripcion','categoria','imagen']
        
   


class CustomUserForm(UserCreationForm): 
    pass 
