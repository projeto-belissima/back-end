from django.db import models


class Vestido(models.Model):
    material = models.CharField(max_length=100)
    descritivo = models.CharField(max_length=200)
    cor = models.CharField(max_length=100)
    descricao = models.TextField(verbose_name="Descrição")
    media_preco = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Faixa de Preço")

    def __str__(self):
        return f"{self.descritivo}"
