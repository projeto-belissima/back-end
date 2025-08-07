from django.db import models

from uploader.models import Image


class Vestido(models.Model):
    material = models.CharField(max_length=100)
    descritivo = models.CharField(max_length=200)
    cor = models.CharField(max_length=100)
    descricao = models.TextField(verbose_name="Descrição")
    media_preco = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Faixa de Preço")
    capa = models.ForeignKey(
        Image,
        related_name='+',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return f"{self.descritivo}"
