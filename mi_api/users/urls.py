from django.urls import path
from .views import RegisterUserView,UserProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),  # Para obtener registrar usuario
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Para obtener tokens
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Para refrescar tokens
    path('profile/', UserProfileView.as_view(), name='profile'), # Para obtener datos del usuario actual
    
]

