from django.db.models import fields
import django_filters
from .models import pedido

class pedidoFiltros(django_filters.FilterSet):

    class Meta:

        model  = pedido
        fields = ["categoria", "cantidad"]