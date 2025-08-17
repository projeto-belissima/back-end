from django.db import models

from uploader.models import Image

from .cor import Cor
from .material import Material


class Vestido(models.Model):
    material = models.ManyToManyField(Material, related_name="vestidos", blank=True)
    descritivo = models.CharField(max_length=200)
    cores = models.ManyToManyField(Cor, related_name="vestidos", blank=True)
    descricao = models.TextField(verbose_name="Descrição")
    media_preco = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Faixa de Preço")
    capa = models.ManyToManyField(
        Image,
        related_name='+',
        blank=True,
        default=None,
    )

    def __str__(self):
        return f"{self.descritivo}"
