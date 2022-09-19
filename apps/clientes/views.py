from multiprocessing import context
from django.shortcuts import render, redirect
from django.views import View
from apps.clientes.models import Cliente
from apps.clientes.forms import formCliente

# Create your views here.

class addCliente(View):
    def get(self,request):
        form = formCliente()
        context = {
            'form':form
        }
        return render(request,'cliente/add.html', context)


    def post(self,request):
        if request.method == "POST":
            form = formCliente(request.POST)
            if form.is_valid():
                form.save()
                return redirect('apps.usuario:login',)  

class viewCliente(View):
    def get(self,request):
        cliente = Cliente.objects.all()
        context = {
            'cliente':cliente
        }
        return render(request, 'cliente/listar.html', context)