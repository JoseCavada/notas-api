from rest_framework import serializers
from .models import Nota

class NotasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = '__all__' # Añade todo los campos del modelo al serializer
        read_only_fields = ('id', 'creado_en','actualizado_en','usuario')
    
    def to_representation(self,instance):# Excluye ciertos campos para que no se vean en la respuesta que haga de JSON
        data= super().to_representation(instance)

        fields_to_exclude = ['usuario']
        for field in fields_to_exclude:
            data.pop(field, None)
        return data
