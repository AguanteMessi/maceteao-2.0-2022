
from dataclasses import field
from rest_framework import serializers
from .models import producto 

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = producto
        fields = ['id', 'nombre', 'precio', 'descripcion','categoria','imagen']


