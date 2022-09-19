from django.db import models


# Create your models here.


class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=70)
    telefono = models.CharField(max_length=12)
    fecha_de_alta = models.DateField()
    usuario = models.CharField(max_length=255)
    # usuario
      



class Suscripcion(models.Model):
    #relacion con cliente
    #vencimiento

    pass