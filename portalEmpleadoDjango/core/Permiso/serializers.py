from rest_framework import serializers
from core.Ausencia.models import Ausencia
from django.contrib.auth.models import User

from core.Permiso.models import Permiso
from core.RRHH.models import Empleado


# Serializa el modelo Ausencia con campos y un hipervínculo a empleado-highlight.
class PermisoSerializer(serializers.HyperlinkedModelSerializer):
    highlight = serializers.HyperlinkedIdentityField(view_name='permiso-highlight', format='html')
    empleado = serializers.HyperlinkedRelatedField(queryset=Empleado.objects.all(), view_name='empleado-detail')
    empleado_nombre = serializers.CharField(source='empleado.nombre', read_only=True)
    class Meta:
        model = Permiso
        fields = ['url', 'id', 'empleado', 'fecha', 'empleado_nombre', 'causa', 'decripcion', 'estado', 'highlight']


# Serializa el modelo Usario
class UserSerializer(serializers.HyperlinkedModelSerializer):
    empleado = serializers.HyperlinkedRelatedField(many=True, view_name='empleado-detail', read_only=True)
    is_staff = serializers.BooleanField(source='is_staff')

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'empleado', 'is_staff']
