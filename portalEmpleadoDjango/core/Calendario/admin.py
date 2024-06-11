from django.contrib import admin
from .models import Calendario, CalendarioItem


class CalendarioItemInline(admin.TabularInline):
    model = CalendarioItem
    extra = 1


class CalendarioAdmin(admin.ModelAdmin):
    list_display = ('empleado', 'anio','nombre')
    inlines = [CalendarioItemInline]
    list_filter = ('anio', 'empleado',)
    search_fields = ('anio', 'empleado',)
    ordering = ('anio','empleado')


class CalendarioItemAdmin(admin.ModelAdmin):
    list_display = ('calendario', 'fecha', 'tipo_dia')
    list_filter = ('calendario', 'tipo_dia', 'fecha', 'calendario__empleado__nombre')
    search_fields = ('calendario__empleado__nombre', 'tipo_dia__nombre')
    # ate_hierarchy = 'fecha'


# class TipoDiaAdmin(admin.ModelAdmin):
#     list_display = ('nombre',)
#     search_fields = ('nombre',)


# admin.site.register(TipoDia, TipoDiaAdmin)
admin.site.register(Calendario, CalendarioAdmin)
admin.site.register(CalendarioItem, CalendarioItemAdmin)
