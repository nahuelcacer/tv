from cProfile import label
from pyexpat import model
from django.db import models
from datetime import date
from apps.servicio.models import Servicio,Plan
from smart_selects.db_fields import ChainedForeignKey


# Create your models here.

class Cliente(models.Model):

    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=70)
    telefono = models.CharField(max_length=12)
    fecha_de_alta = models.DateField()
    usuario = models.CharField(max_length=255) 
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, null=True)
    plan = ChainedForeignKey(Plan,
        chained_field="servicio",
        chained_model_field="servicio",
        show_all=False,
        auto_choose=True,
        sort=True,
        null=True
    )

    def dias_faltantes(self):
        return self.fecha_de_alta - date.today()

class Suscripcion(models.Model):
    dia_comienzo = models.DateField(null=True)
    dia_fin = models.DateField(null=True)
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE,null=True)
    register = models.DateTimeField(auto_now=True, null=True)

    
    



        
