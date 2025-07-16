from rest_framework.serializers import ModelSerializer

from core.models import Encomenda


class EncomendaSerializer(ModelSerializer):
    class Meta:
        model = Encomenda
        fields = "__all__"


class EncomendaListSerializer(ModelSerializer):
    class Meta:
        model = Encomenda
        fields = ("id", "vestido", "emissao", "status", "medidas")
        depth = 2


class EncomendaRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Encomenda
        fields = "__all__"
        depth = 2
