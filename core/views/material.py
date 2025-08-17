from rest_framework.viewsets import ModelViewSet

from core.models import Material
from core.serializers import MaterialSerializer


class MaterialViewSet(ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
