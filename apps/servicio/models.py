from pyexpat import model
from django.db import models

# Create your models here.


class Servicio(models.Model):
    nombre = models.CharField(max_length=60)


class Plan(models.Model):
    nombre = models.CharField(max_length=60)
    fecha = models.DateTimeField(auto_now=True, null=True)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=250, null=True)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)