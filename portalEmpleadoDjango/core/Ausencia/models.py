from django.db import models
from core.RRHH.models import Empleado

class Ausencia(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateField()
    motivo = models.CharField(max_length=100)
    decripcion = models.TextField(null=True, blank=True)
    justificada = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.empleado.nombre} - {self.fecha}"

    class Meta:
        db_table = 'Ausencia'
        verbose_name = 'ausencia'
        verbose_name_plural = 'ausencias'
        ordering = ["id"]
