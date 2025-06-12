from rest_framework.viewsets import ModelViewSet

from core.models import Encomenda
from core.serializers import EncomendaListSerializer, EncomendaRetrieveSerializer, EncomendaSerializer


class EncomendaViewSet(ModelViewSet):
    queryset = Encomenda.objects.all()
    serializer_class = EncomendaSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return EncomendaListSerializer
        elif self.action == "retrieve":
            return EncomendaRetrieveSerializer
        return EncomendaSerializer
