from rest_framework.serializers import ModelSerializer

from core.models import Material


class MaterialSerializer(ModelSerializer):
    class Meta:
        model = Material
        fields = "__all__"
