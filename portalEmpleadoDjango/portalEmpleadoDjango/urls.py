from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from core.Calendario import urls as CalendarioUrls
from core.RRHH import urls as RRHHUrls
from core.Ausencia import urls as AusenciasUrls
from core.Permiso import urls as PermisosUrls

from . import views

schema_view = get_schema_view(
    openapi.Info(
        title="PortalEmpleoDjango API",
        default_version='v1',
        description="PortalEmpleoDjango API description",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="ilarranaga@egibide.org"),
        license=openapi.License(name="Awesome License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [



    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('api/', include(CalendarioUrls)),
    path('api/', include(RRHHUrls)),
    path('api/', include(AusenciasUrls)),
    path('api/', include(PermisosUrls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),



]
