from . import models
from rest_framework import viewsets, permissions, response
from . import serializers

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = models.Productos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.ProductoSerializer
            
class ProductoDetalleViewSet(viewsets.ModelViewSet):
    queryset = models.ProductoDetalles.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.ProductoDetalleSerializer