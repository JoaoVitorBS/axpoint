from django.contrib import admin
from .models import Department, Position, CustomUser
from django.contrib.auth.admin import UserAdmin

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'full_name', 'cpf', 'phone_number', 'department', 'position', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informações Pessoais', {'fields': ('full_name', 'email', 'cpf', 'phone_number', 'employee_code')}),
        ('Informações Profissionais', {'fields': ('department', 'position')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )
    search_fields = ('email', 'full_name', 'cpf', 'employee_code')
    ordering = ('email',)
