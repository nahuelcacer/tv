from datetime import datetime
from django.db import models
from apps.periodo.models import Periodo
from apps.clientes.models import Cliente
# Create your models here.
class Pagos(models.Model):
    saldo = models.IntegerField(null=True)
    importe = models.IntegerField()
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, null=True)
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE, null=True)
    fecha = models.DateField(null=True)

