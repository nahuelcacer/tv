from django.urls import path,include
from .views import addCliente, perfilCliente, viewCliente
from . import views
app_name = 'apps.clientes'

urlpatterns = [
    path('add/',addCliente.as_view(), name="add"),
    path('listar/', viewCliente.as_view(), name='listar'),
    path('perfil/<int:id>',perfilCliente.as_view(), name='perfil'),

]