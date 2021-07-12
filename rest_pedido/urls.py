from django.urls import path
from rest_pedido.views import lista_pedidos, detalle_pedidos

urlpatterns = [
    path('listado/', lista_pedidos, name="listado"),
    path('detalle/<id>', detalle_pedidos, name="detalle"),
]