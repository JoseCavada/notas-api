from django.shortcuts import render #default de views.py

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny,IsAuthenticated # Temporalmente permite acceso sin autenticación

from rest_framework.response import Response
from rest_framework import status

from .models import Nota
from .serializers import NotasSerializer
# Create your views here.

class NotasViewSet(ModelViewSet):
    serializer_class = NotasSerializer
    permission_classes = [IsAuthenticated] 
    def get_queryset(self): # Las notas solo pueden obtenerse de su propio usuario (son personales)  
        user = self.request.user
        queryset = Nota.objects.filter(usuario = user)
        return queryset

    def perform_create(self,serializer): # Hace autor al usuario actual de la nota que se cree
        serializer.save(usuario = self.request.user)
        
    def create(self, request, *args, **kwargs):
        # Llamar al método de creación estándar
        response = super().create(request, *args, **kwargs)

        # Personalizar la respuesta
        data = {
            'respuesta':'Nota creada con éxito',
            'titulo': response.data['titulo'],
            'contenido': response.data['contenido'],
        }

        return Response(data, status=status.HTTP_201_CREATED)
    
    def update(self, request, *args, **kwargs):
        # Buscar el objeto a actualizar
        instance = self.get_object()

        # Llamar al serializer con partial=True para solo actualizar los campos enviados
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        # Validar los datos recibidos
        serializer.is_valid(raise_exception=True)

        # Guardar los datos validados
        serializer.save()

        # Devolver la respuesta con el objeto actualizado
        return Response(serializer.data)