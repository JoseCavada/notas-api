from django.shortcuts import render
from rest_framework.response import Response

from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated

# Create your views here.

User = get_user_model()

class RegisterUserView(CreateAPIView):
    #vista que registra nuevos usuarios
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"email":request.user.email, "username":request.user.username})