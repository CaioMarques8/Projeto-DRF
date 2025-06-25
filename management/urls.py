
from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import home, VagaViewSet, VeiculoViewSet, EstacionamentoViewSet

router = SimpleRouter()
router.register('vagas', VagaViewSet)
router.register('veiculos', VeiculoViewSet)
router.register('estacionamentos', EstacionamentoViewSet)

urlpatterns = [
    path('', home, name='home'),
] + router.urls