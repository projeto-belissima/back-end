from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from core.models import Telefone
from core.serializers import TelefoneSerializer


class TelefoneViewSet(ModelViewSet):
    queryset = Telefone.objects.all()
    serializer_class = TelefoneSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['usuario', 'numero']
