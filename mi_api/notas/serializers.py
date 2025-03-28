from rest_framework import serializers
from .models import Nota

class NotasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = '__all__' #Añade todo los campos del modelo al serializer
        read_only_fields = ('id', 'creado_en','actualizado_en')