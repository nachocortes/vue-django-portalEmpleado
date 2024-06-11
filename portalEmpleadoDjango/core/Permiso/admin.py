from django.contrib import admin
from core.Permiso.models import Permiso


# Admin Departamento
@admin.register(Permiso)
class PermisoAdmin(admin.ModelAdmin):
    list_display = ('empleado', 'fecha', 'causa', 'estado')
    search_fields = ('empleado', 'fecha', 'causa','estado')
    list_filter = ('empleado', 'fecha','causa', 'estado')
    list_display_links = ('empleado',)
    readonly_fields = ('created', 'updated')
    ordering = ('fecha','empleado')
    list_per_page = 8
