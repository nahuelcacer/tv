from email.policy import default
from django.db import models
from datetime import date
from apps.servicio.models import Servicio,Plan
from smart_selects.db_fields import ChainedForeignKey
from django.urls import reverse

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
    suscripcion = models.BooleanField(default=False)

    def dias_faltantes(self):
        return self.fecha_de_alta - date.today()

    def get_absolute_url(self):
        return reverse("apps.clientes:perfil", kwargs={"id": self.id})
    



    
    



        
