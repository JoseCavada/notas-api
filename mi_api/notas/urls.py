from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotasViewSet

router = DefaultRouter()
router.register(r'notas', NotasViewSet, basename='nota')

urlpatterns = [
    path('', include(router.urls)),  # Incluye las rutas generadas automáticamente por el router
]
