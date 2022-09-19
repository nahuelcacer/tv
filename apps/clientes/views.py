from django.shortcuts import render
from django.views import View
from apps.clientes.forms import Cliente

# Create your views here.

class addCliente(View):
    def get(self,request):
        form = Cliente()
        context = {
            'form':form
        }
        return render(request,'cliente/add.html', context)