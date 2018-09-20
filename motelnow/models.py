from django.db import models


class Departamento(models.Model):
    nombre = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.nombre


# Create your models here.
class Hostal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=150)

    latitud = models.DecimalField(max_digits=15, decimal_places=10, null=True, blank=True)
    longitud = models.DecimalField(max_digits=15, decimal_places=10, null=True, blank=True)

    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, blank=True, null=True)

    telefono1 = models.CharField(max_length=12, null=True, blank=True)
    telefono2 = models.CharField(max_length=12, null=True, blank=True)

    precio_minimo = models.IntegerField(default=0)
    precio_maximo = models.IntegerField(default=0)

    activo = models.BooleanField(default=True)


    def __str__(self):
        return self.nombre