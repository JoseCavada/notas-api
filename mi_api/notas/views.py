from django.shortcuts import render #default de views.py

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny  # Temporalmente permite acceso sin autenticación

from rest_framework.response import Response
from rest_framework import status

from .models import Nota
from .serializers import NotasSerializer
# Create your views here.

class NotasViewSet(ModelViewSet):
    queryset = Nota.objects.all()
    serializer_class = NotasSerializer
    permission_classes = [AllowAny] #Por ahora permite a todos que accedan
    def create(self, request, *args, **kwargs):
        # Llamar al método de creación estándar
        response = super().create(request, *args, **kwargs)

        # Personalizar la respuesta
        data = {
            'respuesta':'Nota creada con éxito',
            'titulo': response.data['titulo'],
            'contenido': response.data['contenido'],
            
            # Puedes agregar más campos aquí si es necesario
        }

        return Response(data, status=status.HTTP_201_CREATED)