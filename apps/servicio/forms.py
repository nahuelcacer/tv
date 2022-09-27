from dataclasses import fields
from django import forms
from .models import Servicio, Plan



class FormServicio(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'




class FormPlan(forms.ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'
