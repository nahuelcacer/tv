from datetime import datetime
from multiprocessing import context
from django.shortcuts import render, redirect
from django.views import View
from apps.clientes.models import Cliente, Suscripcion
from apps.clientes.forms import formCliente
import datetime

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
        print(Cliente.objects.latest('fecha_de_alta').nombre)
        context = {
            'cliente':cliente
        }   
        return render(request, 'cliente/listar.html', context)

class perfilCliente(View):
    def get(self,request,id):
        cliente = Cliente.objects.get(id=id)
        suscripciones = Suscripcion.objects.filter(id=id)
        context = {
            'cliente':cliente,
            'suscripciones':suscripciones
        }
        return render(request,'cliente/perfil.html',context)


def agregarSuscripcion(request, id):
    dia_comienzo = datetime.date.today()
    dia_fin = datetime.datetime.now() + datetime.timedelta(30)
    susc = Suscripcion(cliente=Cliente.objects.get(id=id),dia_comienzo=dia_comienzo,dia_fin=dia_fin)
    susc.save()

    
    return redirect('apps.clientes:listar')