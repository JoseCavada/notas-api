from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# Administrador del modelo de usuario
class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        # Crea un usuario normal
        if not email:
            raise ValueError("El usuario debe tener un correo electrónico")

        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)  # Encripta la contraseña
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        # Crea un superusuario con permisos de administrador
        user = self.create_user(email, username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# Modelo de usuario personalizado
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)  # Usuario activo o inactivo
    is_staff = models.BooleanField(default=False)  # Usuario con permisos de admin

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'  # Se usará el email en vez de username para autenticación
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
