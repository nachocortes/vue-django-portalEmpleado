from django.contrib import admin
from django.contrib.auth.models import User
from core.RRHH.models import Empleado, Departamento


# Admin Departamento
@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'id', 'empleados_departamento')
    search_fields = ('nombre', 'telefono', 'id',)
    list_filter = ('nombre', 'telefono')
    list_display_links = ('nombre',)
    readonly_fields = ('created', 'updated')
    ordering = ('nombre',)
    list_per_page = 8

    def empleados_departamento(self, obj):
        return obj.empleado_set.count()

    empleados_departamento.short_description = 'Empleados'


# Admin Empleado
@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'dni', 'departamento', 'edad', 'owner',
                    'id', 'is_staff', 'get_nombre_grupo_usuario')
    search_fields = ('nombre', 'apellido', 'dni', 'departamento__nombre', 'edad',
                     'owner__username', 'is_staff', 'id')
    list_filter = ('nombre', 'apellido', 'dni', 'edad', 'departamento','is_staff')
    list_display_links = ('nombre', 'apellido', 'dni')
    readonly_fields = ('created', 'updated')
    ordering = ('departamento','apellido', 'nombre','is_staff')
    list_per_page = 8

    def get_nombre_grupo_usuario(self, obj):
        if obj.owner:
            return ', '.join([group.name for group in obj.owner.groups.all()])
        return ''

    get_nombre_grupo_usuario.short_description = 'Grupo usuario'
