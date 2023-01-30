from rest_framework import routers
from . import api

router = routers.DefaultRouter()

# prueba = api.ProductoViewSet.as_view({'get':'prueba'})

router.register('api/Productos', api.ProductoViewSet, 'productos')
router.register('api/ProductosDetalles', api.ProductoDetalleViewSet, 'productos_detalles')

urlpatterns = router.urls