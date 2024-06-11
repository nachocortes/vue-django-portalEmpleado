from core.Permiso.views import PermisoViewSet
from core.RRHH import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter


# Crea un enrutador y registra las ViewSets
router = DefaultRouter()

router.register(r'permisos', PermisoViewSet, basename='permiso')
router.register(r'users', views.UserViewSet, basename='user')

# Las URL de API las determina automáticamente el enrutador.
urlpatterns = [
    path('', include(router.urls)),


]
