from rest_framework import serializers
from rest_framework.authtoken.admin import User

from core.Calendario.models import Calendario, CalendarioItem
from core.RRHH.models import Empleado


# Serializa el modelo Departamento con campos y un hipervínculo a empleado-highlight.

class CalendarioSerializer(serializers.HyperlinkedModelSerializer):
    highlight = serializers.HyperlinkedIdentityField(view_name='calendario-highlight', format='html')
    empleado = serializers.HyperlinkedRelatedField(queryset=Empleado.objects.all(), view_name='empleado-detail')
    empleado_nombre = serializers.CharField(source='empleado.nombre', read_only=True)

    class Meta:
        model = Calendario
        fields = ['url', 'id', 'empleado', 'empleado_nombre','nombre', 'anio', 'highlight']


# Serializa el modelo Departamento con campos y un hipervínculo a empleado-highlight.
class CalendarioItemSerializer(serializers.HyperlinkedModelSerializer):
    highlight = serializers.HyperlinkedIdentityField(view_name='calendarioItem-highlight', format='html')
    url = serializers.HyperlinkedIdentityField(view_name="calendarioItem-detail")
    calendario = serializers.HyperlinkedRelatedField(
        queryset=Calendario.objects.all(),
        view_name='calendario-detail'
    )

    class Meta:
        model = CalendarioItem
        fields = ['url', 'id', 'calendario', 'fecha', 'tipo_dia', 'highlight']

# Serializa el modelo Usario
class UserSerializer(serializers.HyperlinkedModelSerializer):
    empleado = serializers.HyperlinkedRelatedField(many=True, view_name='empleado-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'empleado']
