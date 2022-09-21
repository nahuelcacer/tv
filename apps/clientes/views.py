from datetime import datetime
from multiprocessing import context
from django.shortcuts import render, redirect
from django.views import View
from apps.clientes.models import Cliente, Suscripcion
from apps.clientes.forms import formCliente
import datetime

class Clientes():
    def __init__(self,nombre,id,vencimiento):
        self.nombre = nombre
        self.id = id
        self.vencimiento = vencimiento


    def faltan(self):
        return datetime.date.today() - self.vencimiento 
    
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
        cliente_dic = []
        # cliente_dic.fromkeys('nombre', 'id','vencimiento')
        cliente = Cliente.objects.all()
        for i in cliente:
           cliente_dic.append(Clientes(i.nombre,i.id,Suscripcion.objects.filter(cliente=i).latest('dia_fin').dia_fin))

            # arrCliente.append([Suscripcion.objects.filter(cliente=i).latest('dia_fin').dia_fin,i.nombre])
        
        context = {
            'cliente':cliente_dic
        }   
        return render(request, 'cliente/listar.html', context)

class perfilCliente(View):
    def get(self,request,id):
        cliente = Cliente.objects.get(id=id)
        suscripciones = Suscripcion.objects.filter(cliente=cliente)
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