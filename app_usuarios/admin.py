from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    """
    Customização do painel de administração para usuários.
    """
    fieldsets = UserAdmin.fieldsets + (
        ('Informações Adicionais', {'fields': ('tipo', 'foto')}),
    )

admin.site.register(Usuario, UsuarioAdmin)
