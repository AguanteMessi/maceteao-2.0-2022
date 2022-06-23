from email.mime import image
from django import forms
from django.forms import ModelForm
from .models import producto

class productoform(ModelForm):
    class Meta:
        model= producto
        fields =['nombre','precio','descripcion','categoria']
        