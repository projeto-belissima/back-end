from django.db import models

from .user import User


class Endereco(models.Model):
    cep = models.CharField(max_length=9)
    numero = models.IntegerField(null=True, blank=True, verbose_name="Número")
    logradouro = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=2)
    usuario = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="enderecos",
        blank=True,
        null=True,
        verbose_name="Usuário"
    )

    def __str__(self):
        return f"{self.logradouro} - {self.bairro}, {self.cidade}-{self.estado}, {self.cep}"

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"
