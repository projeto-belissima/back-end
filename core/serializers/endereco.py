from rest_framework.serializers import ModelSerializer

from core.models import Endereco


class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = "__all__"
