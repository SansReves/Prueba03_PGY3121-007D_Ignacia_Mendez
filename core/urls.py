from django.urls import path
from .views import eliminar, home, quienes_somos, pedidos, listado, eliminar, modificar, registroUsuarios, cambiarContrasenia





urlpatterns = [
    path('', home, name="home"),
    path('quienes_somos/', quienes_somos, name="quienes_somos"),
    path('pedido/', pedidos, name="pedido"),
    path ('listado/', listado, name="listado"),
    path ('eliminar/<id>/', eliminar, name="eliminar"),
    path ('modificar/<id>/', modificar, name="modificar"),
    path('registroUsuarios/', registroUsuarios, name="registroUsuarios"),
    path('cambiarContrasenia/', cambiarContrasenia, name="cambiarContrasenia"),
]