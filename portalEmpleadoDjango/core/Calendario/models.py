from django.contrib.auth.models import User
from django.db import models


from core.Calendario.choices import TIPO_DIA_CHOICE, TIPO_COLOR_CHOICE
from core.RRHH.models import Empleado


class Calendario(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    anio = models.PositiveSmallIntegerField()
    nombre = models.CharField(max_length=100, unique=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.empleado.nombre} - {self.anio}"
    class Meta:
        db_table = 'Calendarios'
        verbose_name = 'calendario'
        verbose_name_plural = 'calendarios'
        ordering = ['anio','empleado','id']



class CalendarioItem(models.Model):
    calendario = models.ForeignKey(Calendario, on_delete=models.CASCADE)
    fecha = models.DateField()
    tipo_dia = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.calendario.empleado.nombre}/{self.calendario.anio} - {self.fecha} -> {self.tipo_dia}"

    class Meta:
        db_table = 'CalendarioItem'
        verbose_name = 'calendarioItem'
        verbose_name_plural = 'calendarioItems'
        ordering = ["fecha","calendario"]


class TipoDia(models.Model):
    tipo_dia = models.CharField(max_length=50, choices=TIPO_DIA_CHOICE)
    color = models.CharField(max_length=50, choices=TIPO_COLOR_CHOICE)
