from django import forms
<<<<<<< HEAD
from django.forms import ModelForm 
from django.forms import fields
from .models import producto
import datetime 
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm): 
    pass 
=======
from django.forms import ModelForm
from.models import *

class productoform(ModelForm):
    class Meta:
        model= producto
        fields =['nombre','precio','descripcion','categoria']
        models.ImageField(upload_to="productos", null=True)
        
>>>>>>> origin/LUIS
