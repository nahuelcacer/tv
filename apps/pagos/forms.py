from django import forms
from .models import Pagos

class DateInput(forms.DateInput):
    input_type = 'date'

class addPago(forms.ModelForm):
    fecha = forms.DateField(widget=DateInput())
    class Meta:
        model = Pagos
        fields = ['importe', 'periodo', 'fecha']