from .models import Servicio,Plan
from django.core.exceptions import ObjectDoesNotExist

def allServicio():
    return Servicio.objects.all()

def idServicio(id):
    try:
        return Servicio.objects.get(id=id)
    except ObjectDoesNotExist:
        return { 'nombre': 'No existe'}

def idPlan(id):
    try:
        return Plan.objects.get(id=id)

    except ObjectDoesNotExist:
        return { 'nombre': 'No existe'}
