from django.urls import path
from .views import addCliente, viewCliente

#from .views import
app_name = 'apps.clientes'

urlpatterns = [
    path('add/',addCliente.as_view(), name="add"),
    path('listar/', viewCliente.as_view(), name='listar')
]