from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter

from core.views import (
    CorViewSet,
    EncomendaViewSet,
    EnderecoViewSet,
    FuncionarioViewSet,
    MaterialViewSet,
    MedidasViewSet,
    TelefoneViewSet,
    UserViewSet,
    VestidoViewSet,
)
from uploader.router import router as uploader_router

router = DefaultRouter()

router.register(r'cores', CorViewSet, basename='cores')
router.register(r'encomendas', EncomendaViewSet, basename='encomendas')
router.register(r'enderecos', EnderecoViewSet, basename='enderecos')
router.register(r'funcionarios', FuncionarioViewSet, basename='funcionarios')
router.register(r'materiais', MaterialViewSet, basename='materiais')
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
    path('api/media/', include(uploader_router.urls)),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
