from django.db import models



class Munieco(models.Model):
    marca = models.ForeignKey('marca', on_delete=models.CASCADE,)
    munieco = models.CharField(max_length=128)
    precio = models.CharField(max_length=128)
    origen = models.ForeignKey('origen', on_delete=models.CASCADE,)
    anio_fabricacion = models.DateTimeField()

    #def __str__(self):
    #    return f'{self.apellido}, {self.nombre}'


class Ropa(models.Model):
    prenda = models.CharField(max_length=128)
    marca = models.ForeignKey('marca', on_delete=models.CASCADE,)
    talle = models.CharField(max_length=128)
    precio = models.CharField(max_length=128)
    color = models.CharField(max_length=64)

class Marca(models.Model):
    nombre = models.CharField(max_length=128)


class origen(models.Model):
    pais = models.CharField(max_length=128)
