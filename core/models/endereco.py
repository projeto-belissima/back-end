from django.db import models


class Endereco(models.Model):
    cep = models.CharField(max_length=9)
    numero = models.IntegerField(null=True, blank=True)
    logradouro = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.logradouro} - {self.bairro}, {self.cidade}-{self.estado}, {self.cep}"
