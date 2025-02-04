from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .serializers import UsuarioSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

Usuario = get_user_model()

class UsuarioViewSet(viewsets.ModelViewSet):
    """
    API para gerenciamento de usuários.
    Permite listar, criar, editar e excluir usuários.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
