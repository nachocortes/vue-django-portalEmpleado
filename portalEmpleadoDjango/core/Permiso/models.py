from django.db import models
from core.RRHH.models import Empleado


# Create your models here.
class Permiso(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateField()
    causa = models.CharField(max_length=100)
    decripcion = models.TextField(max_length=100,null=True, blank=True)
    estado = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.empleado.nombre} - {self.fecha}"

    class Meta:
        db_table = 'Permiso'
        verbose_name = 'permiso'
        verbose_name_plural = 'permisos'
        ordering = ["id"]
