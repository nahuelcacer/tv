from .models import Servicio,Plan

def allServicio():
    return Servicio.objects.all()