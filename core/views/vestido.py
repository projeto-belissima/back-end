from rest_framework.viewsets import ModelViewSet

from core.models import Vestido
from core.serializers import VestidoSerializer


class VestidoViewSet(ModelViewSet):
    queryset = Vestido.objects.all()
    serializer_class = VestidoSerializer
