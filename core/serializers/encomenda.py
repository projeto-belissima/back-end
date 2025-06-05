from rest_framework.serializers import ModelSerializer

from core.models import Encomenda


class EncomendaSerializer(ModelSerializer):
    class Meta:
        model = Encomenda
        fields = "__all__"
