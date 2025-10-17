"""
Django admin customization.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core.models import (
    Cor,
    Encomenda,
    Endereco,
    Funcionario,
    Material,
    Medidas,
    Telefone,
    User,
    Vestido,
)


@admin.register(Cor)
class CorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'hex')
    search_fields = ('id', 'nome', 'hex')
    list_filter = ('nome',)
    ordering = ('id', 'nome')
    list_per_page = 10


@admin.register(Encomenda)
class EncomendaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'vestido', 'status', 'emissao')
    search_fields = ('usuario', 'vestido', 'status', 'emissao')
    list_filter = ('usuario', 'status', 'emissao')
    ordering = ('usuario', 'vestido', 'status', 'emissao')
    list_per_page = 10


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('cep', 'cidade', 'estado', 'usuario')
    search_fields = ('cep', 'cidade', 'estado', 'usuario')
    list_filter = ('cidade', 'estado', 'usuario')
    ordering = ('cep', 'cidade', 'estado', 'usuario')
    list_per_page = 10


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'usuario', 'setor')
    search_fields = ('cpf', 'usuario', 'cargo', 'setor')
    list_filter = ('usuario', 'setor')
    ordering = ('cpf', 'usuario', 'setor')
    list_per_page = 10


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('id', 'nome')
    list_filter = ('nome',)
    ordering = ('id', 'nome')
    list_per_page = 10


@admin.register(Medidas)
class MedidasAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'titulo')
    search_fields = ('usuario',)
    list_filter = ('usuario',)
    ordering = ('usuario', 'titulo')
    list_per_page = 10


@admin.register(Telefone)
class TelefoneAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'ddd', 'numero')
    search_fields = ('usuario', 'numero')
    list_filter = ('usuario',)
    ordering = ('usuario', 'ddd', 'numero')
    list_per_page = 10


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""

    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name', 'passage_id', 'foto')}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            },
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
        (_('Groups'), {'fields': ('groups',)}),
        (_('User Permissions'), {'fields': ('user_permissions',)}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email',
                    'password1',
                    'password2',
                    'name',
                    'is_active',
                    'is_staff',
                    'is_superuser',
                ),
            },
        ),
    )


@admin.register(Vestido)
class VestidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descritivo',)
    search_fields = ('id', 'descritivo', 'material')
    list_filter = ('descritivo', 'material')
    ordering = ('id', 'descritivo', 'material')
    list_per_page = 10
