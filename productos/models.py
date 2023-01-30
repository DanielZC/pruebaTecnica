from django.db import models

# Create your models here.

class Productos(models.Model):
    nombre = models.CharField(max_length=50, default='')
    codigo = models.IntegerField(editable=False, unique=True)
    descripcion = models.TextField(null=False, default='')
    precio = models.IntegerField(default=0)
    
class ProductoDetalles(models.Model):
    producto_id = models.ForeignKey(Productos, on_delete=models.SET_NULL, default=0, null=True)
    cantidad = models.IntegerField(default=0)
    valorTotal = models.IntegerField(default=0)
    valorIva = models.IntegerField(default=0)