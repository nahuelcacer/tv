from django.db import models

# Create your models here.

class Periodo(models.Model):
    inicio = models.DateField(null=True)
    fin = models.DateField(null=True)
    nombre = models.CharField(max_length=255)
    

    def __str__(self):
        return self.nombre + " " + self.inicio.strftime('%Y')
    