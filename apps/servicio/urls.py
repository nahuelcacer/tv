from django.urls import path,include
from .views import ViewServicio
from . import views

app_name = 'apps.servicio'

urlpatterns = [
    path('', views.MainServicio ,name="main"),
    path('add/', ViewServicio.as_view(), name="add"),
    path('ver/<int:id>', views.IdServicio , name="ver"),

    # path('ver/<int:id>',name="ver")

]