from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter

from core.views import EnderecoViewSet, FuncionarioViewSet, MedidasViewSet, TelefoneViewSet, UserViewSet, VestidoViewSet

router = DefaultRouter()

router.register(r'enderecos', EnderecoViewSet, basename='enderecos')
router.register(r'funcionarios', FuncionarioViewSet, basename='funcionarios')
router.register(r'medidas', MedidasViewSet, basename='medidas')
router.register(r'telefones', TelefoneViewSet, basename='telefones')
router.register(r'usuarios', UserViewSet, basename='usuarios')
router.register(r'vestidos', VestidoViewSet, basename="vestidos")

urlpatterns = [
    path('admin/', admin.site.urls),
    # OpenAPI 3
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
    # API
    path('api/', include(router.urls)),
]
