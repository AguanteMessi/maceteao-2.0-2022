from django import forms
from django.forms import ModelForm 
from django.forms import fields
from .models import producto
import datetime 
from django.contrib.auth.forms import UserCreationForm
from.models import *

class CustomUserForm(UserCreationForm): 
    pass 


class productoform(ModelForm):
    class Meta:
        model= producto
        fields =['nombre','precio','descripcion','categoria']
        models.ImageField(upload_to="productos", null=True)
        
