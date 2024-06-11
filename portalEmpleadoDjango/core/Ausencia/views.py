from rest_framework import viewsets, renderers
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.Ausencia import permissions
from core.Ausencia.models import Ausencia
from core.Ausencia.serializers import AusenciaSerializer, UserSerializer
from django.contrib.auth.models import User

class AusenciaViewSet(viewsets.ModelViewSet):
    queryset = Ausencia.objects.all()
    serializer_class = AusenciaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Añade rutas personalizadas a las acciones de tu viewset.
    # Permite definir métodos adicionales que pueden ser invocados desde la API
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        ausencia = self.get_object()
        return Response(ausencia.highlighted)

class UserAusenciaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AusenciaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Ausencia.objects.filter(empleado=self.request.user.empleado)
