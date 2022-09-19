from django import forms
from .models import Cliente

class Cliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'telefono', 'direccion', 'fecha_de_alta']
