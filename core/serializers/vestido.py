from rest_framework.serializers import ModelSerializer

from core.models import Vestido


class VestidoSerializer(ModelSerializer):
    class Meta:
        model = Vestido
        fields = "__all__"
