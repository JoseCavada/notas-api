from django.db import models

# Create your models here.

class Nota(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    creado_en = models.DateTimeField(auto_now_add=True)  # Solo cuando se crea
    actualizado_en = models.DateTimeField(auto_now=True)  # Se actualiza cada vez que se guarda

    def __str__(self):
        return self.titulo
