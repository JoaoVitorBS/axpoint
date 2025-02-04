from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    TIPO_USUARIO = [
        ('admin', 'Administrador'),
        ('operador', 'Operador'),
        ('cliente', 'Cliente'),
    ]
    
    tipo = models.CharField(max_length=20, choices=TIPO_USUARIO, default='cliente')
    foto = models.ImageField(upload_to='usuarios/', null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.get_tipo_display()})"
