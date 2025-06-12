from rest_framework.viewsets import ModelViewSet

from core.models import Medidas
from core.serializers import MedidasSerializer


class MedidasViewSet(ModelViewSet):
    queryset = Medidas.objects.all()
    serializer_class = MedidasSerializer
