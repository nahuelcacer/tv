from django import forms
from .models import Cliente
class Cliente(forms.ModelForm):
    fecha_de_alta = forms.DateField()
    class Meta:
        model = Cliente
        fields = ['nombre', 'telefono', 'direccion', 'fecha_de_alta']
