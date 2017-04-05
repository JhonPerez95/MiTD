from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from colorful.fields import RGBColorField
from django.core.urlresolvers import reverse, reverse_lazy


class Torneo(models.Model):
    descripcion = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (self.descripcion)


class Equipo(models.Model):
    nombre = models.CharField(max_length=200)
    color = RGBColorField()
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (self.nombre)

class Jugador(models.Model):
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    documento = models.IntegerField()
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (self.nombres, self.apellidos)