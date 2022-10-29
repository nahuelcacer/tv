from django.urls import path,include
from . import views
from .views import ListarPagos, Pago
app_name = 'apps.pagos'

urlpatterns = [
    path('<int:id>/add/', Pago.as_view(), name="add" ),
    path('<int:id>/listar-pagos/<str:periodo>', ListarPagos.as_view(), name="listar" )
]