from django.contrib.auth.models import User
from django.db import models

# Modelo Departamento
class Departamento(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    telefono = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "departamentos"
        verbose_name = "departamento"
        ordering = ["-created"]

# Modelo Empleado
class Empleado(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='empleado', blank=True, null=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=50, unique=True)
    edad = models.IntegerField()
    owner = models.ForeignKey(User, related_name='empleados', on_delete=models.CASCADE, null=True)
    is_staff = models.BooleanField(default=False)
    highlighted = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if self.owner:
            self.is_staff = self.owner.is_staff
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "empleados"
        verbose_name = "empleado"
        ordering = ["-created"]
