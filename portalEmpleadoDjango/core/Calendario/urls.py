from core.Calendario import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.Calendario.views import UserCalendarioViewSet

# Crea un enrutador y registra las ViewSets
router = DefaultRouter()

router.register(r'calendarios', views.CalendarioViewSet, basename='calendario')
router.register(r'calendarioItems', views.CalendarioItemViewSet, basename='calendarioItem')
router.register(r'user/calendarios', UserCalendarioViewSet, basename='user-calendarios')
router.register(r'users', views.UserViewSet, basename='user')

# Las URL de API las determina automáticamente el enrutador.
urlpatterns = [
    path('', include(router.urls)),

]
