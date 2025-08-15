from django.db import models

from .cor import Cor
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
    vestido = models.ForeignKey(Vestido, related_name="encomendas", on_delete=models.PROTECT, null=True, blank=True)
    cor = models.ForeignKey(Cor, related_name="encomendas", on_delete=models.PROTECT, null=True, blank=True)
    emissao = models.DateField(auto_now_add=True, verbose_name="Data de emissão")
    retirada = models.DateField(null=True, blank=True, verbose_name="Data de retirada")
    status = models.IntegerField(choices=Status.choices, default=Status.ENCOMENDADO)
    medidas = models.ForeignKey(Medidas, related_name="encomendas", on_delete=models.PROTECT)
    observacoes = models.TextField(null=True, blank=True, verbose_name="Observações")
    preco = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name="Preço acertado")

    def __str__(self):
        return f"{self.id} - {self.usuario.name} {self.emissao}"
