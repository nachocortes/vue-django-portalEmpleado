from core.Ausencia.views import AusenciaViewSet
from core.RRHH import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter


# Crea un enrutador y registra las ViewSets
router = DefaultRouter()

router.register(r'ausencias', AusenciaViewSet, basename='ausencia')
router.register(r'users', views.UserViewSet, basename='user')

# Las URL de API las determina automáticamente el enrutador.
urlpatterns = [
    path('', include(router.urls)),


]
