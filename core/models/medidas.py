from django.db import models

from .user import User


class Medidas(models.Model):
    usuario = models.ForeignKey(User, related_name="medidas", on_delete=models.CASCADE, verbose_name="Usuário")
    data_medicao = models.DateField(auto_now_add=True)
    titulo = models.CharField(max_length=40, verbose_name="Título", default="Título")
    descricao = models.CharField(max_length=100, verbose_name="Descrição", null=True, blank=True)
    busto_circunferencia = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=1,
        verbose_name="Circunferência do busto"
    )
    cintura_circunferencia = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=1,
        verbose_name="Circunferência da cintura"
    )
    quadril_circunferencia = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=1,
        verbose_name="Circunferência do quadril"
    )
    punho_circunferencia = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=1,
        verbose_name="Circunferência do punho"
    )
    ombro_altura = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=1,
        verbose_name="Altura do ombro"
    )
    braco_comprimento = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=1,
        verbose_name="Comprimento do braço"
    )

    def __str__(self):
        return f"{self.id} - {self.usuario.name} {self.titulo}"

    class Meta:
        verbose_name = "Medida"
        verbose_name_plural = "Medidas"
