from django import forms
<<<<<<< HEAD
from django.forms import ModelForm
from.models import *
=======
>>>>>>> origin/pedro
from django.forms import ModelForm 
from django.forms import fields
from .models import producto
import datetime 
from django.contrib.auth.forms import UserCreationForm
<<<<<<< HEAD
=======
from.models import *

class CustomUserForm(UserCreationForm): 
    pass 

>>>>>>> origin/pedro

class productoform(ModelForm):
    class Meta:
        model= producto
        fields=['nombre','precio','descripcion','categoria','imagen']
        
<<<<<<< HEAD
        


class CustomUserCreationForm(UserCreationForm): 
    pass 
=======
>>>>>>> origin/pedro
