from rest_framework.viewsets import ModelViewSet

from core.models import Encomenda
from core.serializers import EncomendaSerializer


class EncomendaViewSet(ModelViewSet):
    queryset = Encomenda.objects.all()
    serializer_class = EncomendaSerializer
