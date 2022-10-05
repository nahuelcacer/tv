from django.urls import path,include
from .views import UpdatePlan, ViewServicio
from . import views

app_name = 'apps.servicio'

urlpatterns = [
    path('', views.MainServicio ,name="main"),
    path('add/', ViewServicio.as_view(), name="add"),
    path('ver/<int:id>', views.IdServicio , name="ver"),
    path('ver/<int:id>/addplan', views.addplan , name="addplan"),
    path('edit/<int:pk>', UpdatePlan.as_view() , name="editplan"),


    # path('ver/<int:id>',name="ver")

]