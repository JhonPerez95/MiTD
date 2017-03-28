from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from colorful.fields import RGBColorField


class Torneo(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	descripcion = models.CharField(max_length=200)

	def __str__(self):
		return (self.descripcion)


class Jugador(models.Model):
	nombres = models.CharField(max_length=200)
	apellidos = models.CharField(max_length=200)
	documento = models.IntegerField()
	user = models.ForeignKey(settings.AUTH_USER_MODEL)

	def __str__(self):
		return (self.nombres, self.apellidos)
		

class Equipo(models.Model):
	nombre = models.CharField(max_length=200)
	color = RGBColorField()
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	jugador = models.ForeignKey(Jugador)

	def __str__(self):
		return (self.nombre)