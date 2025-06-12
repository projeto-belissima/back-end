from rest_framework.serializers import ModelSerializer

from core.models import Medidas


class MedidasSerializer(ModelSerializer):
    class Meta:
        model = Medidas
        fields = "__all__"
