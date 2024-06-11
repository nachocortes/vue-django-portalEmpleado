from core.RRHH import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.RRHH.views import EmpleadoViewSet



# Crea un enrutador y registra las ViewSets
router = DefaultRouter()

router.register(r'empleados', EmpleadoViewSet, basename='empleado')
router.register(r'departamentos', views.DepartamentoViewSet, basename='departamento')
router.register(r'users', views.UserViewSet, basename='user')

# Las URL de API las determina automáticamente el enrutador.
urlpatterns = [
    path('', include(router.urls)),


]
