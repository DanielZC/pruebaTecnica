from django.urls import path
from . import views

urlpatterns = [
    path('api/Productos/', views.productos),
    path('api/Producto/<int:identificador>/', views.producto),
    path('api/Producto/Crear/', views.crear),
    path('api/Producto/Editar/<int:id>/', views.editar),
    path('api/Producto/Eliminar/<int:id>/', views.eliminar),
    
    path('api/ProductosDetalles/', views.detalles),
    path('api/ProductoDetalle/<int:id>/', views.detalle),
    path('api/ProductoDetalle/Crear/', views.crearDetalle),
    path('api/ProductoDetalle/Editar/<int:id>/', views.editarDetalle),
    path('api/ProductoDetalle/Eliminar/<int:id>/', views.eliminarDetalle),
]