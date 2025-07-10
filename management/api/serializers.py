from rest_framework.serializers import ModelSerializer

from management.models import Estacionamento, Vaga, Veiculo


class VagaSerializer(ModelSerializer):
    class Meta:
        model = Vaga
        fields = ["id", "codigo", "disponivel"]


class VeiculoSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ["id", "placa", "modelo"]


class EstacionamentoSerializer(ModelSerializer):
    class Meta:
        model = Estacionamento
        fields = ["id", "veiculo", "vaga", "entrada", "saida", "valor_pago"]
