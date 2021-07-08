from django.shortcuts import render
from .serializers import usuarioSerializer
from core.models import usuario
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def usuarios(request):
    """
    Lista todos los usuarios
    """
    if request.method == 'GET':
        usuarios = usuario.objects.all()
        serializer = usuarioSerializer(usuarios, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        """
        Agrega un usuario
        """
        data = JSONParser().parse(request) 
        serializer = usuarioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_usuario(request, em ):
    try:
        detalle_usuario = usuario.objects.get(email=em)
    except usuario.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    """
    GET: Mostrar detalle de un usuario según patente
    """
    if request.method == 'GET':
        serializer = usuarioSerializer(detalle_usuario)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        """
        PUT: Editar un vehiculo por patente
        """
        data = JSONParser().parse(request)
        serializer = usuarioSerializer(detalle_usuario, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        """
        DELETE: Borrar un usuario por patente
        """
        detalle_usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)