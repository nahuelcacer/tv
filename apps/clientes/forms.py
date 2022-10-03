from django import forms
from .models import Cliente
from apps.servicio.models import Plan,Servicio

class DateInput(forms.DateInput):
    input_type = 'date'
    

class formCliente(forms.ModelForm):
    
    fecha_de_alta = forms.DateField(widget=DateInput())
    class Meta:
        model = Cliente
        fields = ['nombre', 'telefono', 'direccion', 'fecha_de_alta', 'usuario','servicio' ,'plan']
