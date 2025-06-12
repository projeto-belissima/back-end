from rest_framework.viewsets import ModelViewSet

from core.models import Funcionario
from core.serializers import FuncionarioSerializer


class FuncionarioViewSet(ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
