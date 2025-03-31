from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()  # Obtiene el modelo de usuario configurado en AUTH_USER_MODEL, por si cambia es mejor dejarlo así

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}


    def create (self, validated_data): # Al hacer un post para crear, lo crea mediante la funcion de create_user que se define en el modelo (esto es para encriptar la contraseña)
        user = User.objects.create_user(**validated_data)
        return user
    
    
