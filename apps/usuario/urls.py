from django.urls import path
from django.contrib.auth.views import LoginView

#from .views import
app_name = 'apps.usuario'

urlpatterns = [
    path('login/', LoginView.as_view(template_name="usuario/login.html"), name="login"),
]