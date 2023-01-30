from rest_framework import serializers
from . import models

class ProductoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Productos
        fields = ('nombre', 'descripcion', 'precio')
        
class ProductoDetalleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.ProductoDetalles
        fields = ('producto_id', 'cantidad', 'valorTotal', 'valorIva')
        