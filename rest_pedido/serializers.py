from rest_framework import serializers
from core.models import pedido

class pedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = pedido
        fields = ['nombre','categoria','cantidad','comentario','imagen']