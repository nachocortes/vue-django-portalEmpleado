from rest_framework import viewsets, renderers
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.Permiso import permissions
from core.Permiso.models import Permiso
from core.Permiso.serializers import PermisoSerializer, UserSerializer
from django.contrib.auth.models import User

class PermisoViewSet(viewsets.ModelViewSet):
    queryset = Permiso.objects.all()
    serializer_class = PermisoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Añade rutas personalizadas a las acciones de tu viewset.
    # Permite definir métodos adicionales que pueden ser invocados desde la API
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        permiso = self.get_object()
        return Response(permiso.highlighted)

class UserPermisoViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PermisoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Permiso.objects.filter(empleado=self.request.user.empleado)
