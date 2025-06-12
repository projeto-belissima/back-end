from django.db import models

from .user import User


class Medidas(models.Model):
    usuario = models.ForeignKey(User, related_name="medidas", on_delete=models.CASCADE, verbose_name="Usuário")
    data_medicao = models.DateField(auto_now_add=True)
    altura = models.DecimalField(max_digits=5, decimal_places=2)
    busto_altura = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Altura do busto"
    )
    busto_circunferencia = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Circunferência do busto"
    )
    cintura_altura = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Altura da cintura"
    )
    cintura_circunferencia = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Circunferência da cintura"
    )
    quadril_altura = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Altura do quadril"
    )
    quadril_circunferencia = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Circunferência do quadril"
    )
    costas_largura = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Largura das costas"
    )
    ombro_comprimento = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Comprimento do ombro"
    )

    def __str__(self):
        return f"{self.id} - {self.usuario.name} {self.data_medicao}"

    class Meta:
        verbose_name = "Medida"
        verbose_name_plural = "Medidas"
