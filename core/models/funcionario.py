from django.db import models

from .user import User


class Funcionario(models.Model):
    usuario = models.ForeignKey(User, related_name="funcionarios", on_delete=models.PROTECT, verbose_name="Usuário")
    cpf = models.CharField(max_length=14, unique=True, verbose_name="CPF")
    formacao = models.CharField(max_length=100, verbose_name="Formação")
    cargo = models.CharField(max_length=100)
    setor = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id} {self.usuario.name}"

    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionário"
