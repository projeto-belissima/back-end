from django.db import models

from .medidas import Medidas
from .user import User
from .vestido import Vestido


class Encomenda(models.Model):
    class Status(models.IntegerChoices):
        ENCOMENDADO = 0, "Encomendado"
        INICIADO = 1, "Iniciada produção"
        PRONTO = 2, "Pronto"
        PAGO = 3, "Pago"
        DESCARTADO = 4, "Descartado"

    usuario = models.ForeignKey(User, related_name="encomendas", on_delete=models.PROTECT, verbose_name="Usuário")
    vestido = models.ManyToManyField(Vestido, related_name="encomendas", blank=True)
    emissao = models.DateField(auto_now_add=True, verbose_name="Data de emissão")
    status = models.IntegerField(choices=Status.choices, default=Status.ENCOMENDADO)
    medidas = models.ForeignKey(Medidas, related_name="encomendas", on_delete=models.PROTECT)
    vestido_comprimento = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Comprimento do vestido"
    )
    manga_comprimento = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Comprimento da manga"
    )
    # tamanho = models.

    def __str__(self):
        return f"{self.id} - {self.usuario.name} {self.emissao}"
