from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Informações Adicionais', {'fields': ('tipo', 'foto')}),
    )
    list_display = ['username', 'email', 'tipo', 'is_active', 'is_staff']
    list_filter = ['tipo', 'is_active', 'is_staff']
    search_fields = ['username', 'email']

admin.site.register(Usuario, UsuarioAdmin)
