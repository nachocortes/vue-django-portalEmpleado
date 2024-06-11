from django.contrib import admin
from core.Ausencia.models import Ausencia


@admin.register(Ausencia)
class AusenciaAdmin(admin.ModelAdmin):
    list_display = ('empleado', 'fecha', 'motivo', 'justificada')
    search_fields = ('empleado', 'fecha', 'motivo', 'justificada')
    list_filter = ('empleado', 'fecha', 'motivo', 'justificada')
    list_display_links = ('empleado',)
    readonly_fields = ('created', 'updated')
    ordering = ('fecha', 'empleado')
    list_per_page = 8
