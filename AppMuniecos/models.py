from django.db import models
from datetime import date

# Create your models here.

class Usuarios(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    email = models.EmailField()

class muniecos(models.Model):
    marca = models.ForeignKey('marcas', on_delete=models.CASCADE,)
    munieco = models.CharField(max_length=128)
    precio = models.CharField(max_length=128)
    origen = models.ForeignKey('origen', on_delete=models.CASCADE,)
    anio_fabricacion = models.DateTimeField()

    #def __str__(self):
    #    return f'{self.apellido}, {self.nombre}'


class ropa(models.Model):
    prenda = models.CharField(max_length=128)
    marca = models.ForeignKey('marcas', on_delete=models.CASCADE,)
    talle = models.CharField(max_length=128)
    precio = models.CharField(max_length=128)
    color = models.CharField(max_length=64)

class marcas(models.Model):
    nombre = models.CharField(max_length=128)


class origen(models.Model):
    pais = models.CharField(max_length=128)
