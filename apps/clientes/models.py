from pyexpat import model
from django.db import models
from datetime import date

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=70)
    telefono = models.CharField(max_length=12)
    fecha_de_alta = models.DateField()
    usuario = models.CharField(max_length=255)

    def dias_faltantes(self):
        return self.fecha_de_alta - date.today()

class Suscripcion(models.Model):
    dia_comienzo = models.DateField(null=True)
    dia_fin = models.DateField(null=True)
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE,null=True)
    register = models.DateTimeField(auto_now=True, null=True)

    
        

class Servicio(models.Model):
    dia_comienzo = models.DateField(null=True)
    dia_fin = models.DateField(null=True)
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE, null=True )



        
