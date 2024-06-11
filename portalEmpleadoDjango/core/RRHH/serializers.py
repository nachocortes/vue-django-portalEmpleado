from rest_framework import serializers
from core.RRHH.models import Empleado, Departamento
from django.contrib.auth.models import User


# Serializa el modelo Departamento con campos y un hipervínculo a empleado-highlight.
class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    highlight = serializers.HyperlinkedIdentityField(view_name='departamento-highlight', format='html')

    class Meta:
        model = Departamento
        fields = ['url', 'id', 'nombre', 'telefono', 'highlight']


# Serializa el modelo Empleados
class EmpleadoSerializer(serializers.HyperlinkedModelSerializer):
    highlight = serializers.HyperlinkedIdentityField(view_name='empleado-highlight', format='html')
    departamento = serializers.HyperlinkedRelatedField(view_name='departamento-detail',
                                                       queryset=Departamento.objects.all()
                                                       )
    departamento_nombre = serializers.CharField(source='departamento.nombre', read_only=True)

    class Meta:
        model = Empleado
        fields = ['url', 'id', 'nombre', 'apellido', 'dni', 'edad', 'departamento', 'departamento_nombre', 'is_staff',
                  'highlight']


# Serializa el modelo Usario
class UserSerializer(serializers.HyperlinkedModelSerializer):
    empleado = serializers.HyperlinkedRelatedField(many=True, view_name='empleado-detail', read_only=True)
    is_staff = serializers.BooleanField(source='is_staff')

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'empleado', 'is_staff']
