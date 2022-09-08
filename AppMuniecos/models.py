from django.db import models

class Munieco(models.Model):
    tipo = models.CharField(max_length=128)
    origen = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.tipo} - {self.origen}'

class Ropa(models.Model):
    prenda = models.CharField(max_length=64)
    talle = models.IntegerField()
    
    def __str__(self):
        return f'{self.prenda} - {self.talle}'

class Marca(models.Model):
    nombre = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.nombre}'


    