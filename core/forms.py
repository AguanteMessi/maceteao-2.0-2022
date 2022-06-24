from django import forms
from django.forms import ModelForm
from.models import *

class productoform(ModelForm):
    class Meta:
        model= producto
        fields =['nombre','precio','descripcion','categoria']
        models.ImageField(upload_to="productos", null=True)
        