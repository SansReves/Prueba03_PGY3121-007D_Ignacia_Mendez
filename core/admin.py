from django.contrib import admin
from .models import pedido, categoria

# Register your models here.

class detalleCategoria(admin.ModelAdmin):
    search_fields = ["nombre"]
    list_display = ["nombre","descripcion"]

class detallePedido(admin.ModelAdmin):
    search_fields =["nombre","id"]
    list_per_page = 30 #paginacion
    list_display = ["id","nombre","correo","categoria","cantidad","comentario","imagen"]
    list_filter = ["categoria","cantidad"]

admin.site.register(pedido,detallePedido)
admin.site.register(categoria, detalleCategoria)
