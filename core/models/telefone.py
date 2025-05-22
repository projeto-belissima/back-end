from django.db import models

from .user import User


class Telefone(models.Model):
    usuario = models.ForeignKey(User, related_name="telefones", on_delete=models.PROTECT, verbose_name="Usuário")
    ddd = models.IntegerField(verbose_name="DDD")
    numero = models.CharField(max_length=10, verbose_name="Número")

    def __str__(self):
        return f"({self.ddd}) {self.numero}"
