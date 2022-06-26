from django import forms
from django.forms import ModelForm
from.models import *
from django.forms import ModelForm 
from django.forms import fields
from .models import producto
import datetime 
from django.contrib.auth.forms import UserCreationForm

class productoform(ModelForm):
    class Meta:
        model= producto
        fields=['nombre','precio','descripcion','categoria','imagen']
        
        


class CustomUserCreationForm(UserCreationForm): 
    pass 
