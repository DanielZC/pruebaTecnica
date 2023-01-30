from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q

from . import models
from . import serializers

# Create your views here.

# PRODUCTOS

@api_view(['GET'])
def productos(request):
    productos = models.Productos.objects.all()
    serializer = serializers.ProductoSerializer(productos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def producto(resquest, identificador):
    producto = models.Productos.objects.get(id=identificador)
    serializer = serializers.ProductoSerializer(producto, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def crear(request):
    data = request.data
    producto = models.Productos.objects.create(
        nombre = data['nombre'],
        codigo = data['codigo'],
        descripcion = data['descripcion'],
        precio = data['precio']
    )
    serializer = serializers.ProductoSerializer(producto, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def editar(request, id):
    data = request.data
    producto = models.Productos.objects.get(id=id)
    serializer = serializers.ProductoSerializer(producto, data=data)
    if(serializer.is_valid()):
        serializer.save()
        return Response(serializer.data)
    
@api_view(['DELETE'])
def eliminar(request, id):
    producto = models.Productos.objects.get(id=id)
    producto.delete()
    return Response('Producto eliminado')

# PRODUCTO DETALLES

@api_view(['GET'])
def detalles(request):
    productosDetalles = models.ProductoDetalles.objects.all()
    serializer = serializers.ProductoDetalleSerializer(productosDetalles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detalle(resquest, id):
    productoDetalle = models.ProductoDetalles.objects.get(id=id)
    serializer = serializers.ProductoDetalleSerializer(productoDetalle, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def crearDetalle(request):
    data = request.data
    producto = models.Productos.objects.get(id=data['producto_id'])
    productoDetalle = models.ProductoDetalles.objects.create(
        producto_id = producto,
        cantidad = data['cantidad'],
        valorTotal = data['valorTotal'],
        valorIva = data['valorIva']
    )
    serializer = serializers.ProductoDetalleSerializer(productoDetalle, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def editarDetalle(request, id):
    data = request.data
    
    productoDetalle = models.ProductoDetalles.objects.get(id=id)
    serializer = serializers.ProductoDetalleSerializer(productoDetalle, data=data)
    if(serializer.is_valid()):
        serializer.save()
        return Response(serializer.data)
    
@api_view(['DELETE'])
def eliminarDetalle(request, id):
    productoDetalle = models.ProductoDetalles.objects.get(id=id)
    productoDetalle.delete()
    return Response('Producto detalle eliminado')