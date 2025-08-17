from django.db import models


class Material(models.Model):
    nome = models.CharField(max_length=45)

    def __str__(self):
        return f"{self.id} - {self.nome}"

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materiais"
