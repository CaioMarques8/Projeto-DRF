# pylint: disable=no-member
import uuid

from django.db import models


class Vaga(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        status = "Disponível" if self.disponivel else "Ocupada"
        return f"Vaga {self.codigo} - {status}"


class Veiculo(models.Model):
    placa = models.CharField(max_length=10, unique=True)
    modelo = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.modelo} ({self.placa})"


class Estacionamento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    entrada = models.DateTimeField(auto_now_add=True)
    saida = models.DateTimeField(null=True, blank=True)
    valor_pago = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.veiculo.placa} na {self.vaga.codigo}"
