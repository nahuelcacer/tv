from django.urls import path
from .views import addCliente

#from .views import
app_name = 'apps.usuario'

urlpatterns = [
    path('add/',addCliente.as_view(), name="add"),
]