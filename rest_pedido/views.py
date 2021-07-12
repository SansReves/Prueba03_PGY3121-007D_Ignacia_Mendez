from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from core.models import pedido  
from .serializers import pedidoSerializer

@csrf_exempt
@api_view(['GET', 'POST'])
def lista_pedidos(request):
    #listado
    if request.method == 'GET':
        ped  = pedido.objects.all()
        serializer = pedidoSerializer(ped, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = pedidoSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



@csrf_exempt
@api_view(['GET','PUT', 'DELETE'])
def detalle_pedidos(request, id):
    try:
        ped = pedido.objects.get(id = id)
    except pedido.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = pedidoSerializer(ped)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request) #transformamos los datos en formato JSON
        serializer = pedidoSerializer(ped, data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        ped.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)