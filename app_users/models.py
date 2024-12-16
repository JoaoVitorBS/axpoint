# app_users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

# Modelo para os Departamentos
class Departamento(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome do Departamento")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"


# Modelo para as Funções
class Funcao(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome da Função")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Função"
        verbose_name_plural = "Funções"


# Modelo de Usuário Personalizado
class Usuario(AbstractUser):
    nome_completo = models.CharField(max_length=255, verbose_name="Nome Completo")
    cpf = models.CharField(max_length=14, unique=True, verbose_name="CPF")
    telefone = models.CharField(max_length=15, verbose_name="Telefone")
    codigo_funcionario = models.CharField(max_length=10, unique=True, verbose_name="Código do Funcionário")

    funcao = models.ForeignKey(
        'Funcao',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Função"
    )
    departamento = models.ForeignKey(
        'Departamento',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Departamento"
    )

    grupos = models.ManyToManyField(
        'auth.Group',
        related_name='usuario_grupos',
        blank=True,
        verbose_name="Grupos"
    )
    permissoes = models.ManyToManyField(
        'auth.Permission',
        related_name='usuario_permissoes',
        blank=True,
        verbose_name="Permissões"
    )

    def __str__(self):
        return self.nome_completo or self.username

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
