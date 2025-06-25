from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .models import Vaga, Veiculo, Estacionamento
from .api.serializers import VagaSerializer, VeiculoSerializer, EstacionamentoSerializer

from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <h1>Sistema de Estacionamento</h1>
        <p>API Endpoints:</p>
        <ul>
            <li><a href="/api/vagas/">Vagas</a></li>
            <li><a href="/api/veiculos/">Veículos</a></li>
            <li><a href="/api/estacionamentos/">Estacionamentos</a></li>
            <li><a href="/admin/">Admin</a></li>
        </ul>
    """)

class VagaViewSet(ModelViewSet):
    queryset = Vaga.objects.all()
    serializer_class = VagaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
    permission_classes = [permissions.IsAuthenticated]

class EstacionamentoViewSet(ModelViewSet):
    queryset = Estacionamento.objects.all()
    serializer_class = EstacionamentoSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        vaga = serializer.validated_data['vaga']
        vaga.disponivel = False
        vaga.save()
        serializer.save()
    
    def perform_destroy(self, instance):
        vaga = instance.vaga
        vaga.disponivel = True
        vaga.save()
        instance.delete()