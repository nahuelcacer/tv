from datetime import date, datetime
from multiprocessing import context
from operator import attrgetter
from django.shortcuts import render, redirect
from django.views import View
from apps.clientes.models import Cliente, Suscripcion
from apps.clientes.forms import formCliente
import datetime
from apps.clientes.tools.queries import Queries
class Clientes():
    """Crea objeto de clientes para enviar en el context"""
    def __init__(self,nombre,id,vencimiento):
        self.nombre = nombre
        self.id = id
        self.vencimiento = vencimiento


    def faltan(self):
        if self.vencimiento != 0:
            venc = self.vencimiento - datetime.date.today()  
            return int(venc.days)
        else:
            return "Sin suscripcion"
    def p_vencimiento(self):
        """Fecha transformada a str"""
        if self.vencimiento != 0:
            return self.vencimiento.strftime('%d/%m/%Y')
        else: 
            return ""

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
    """Clase para listar clientes"""
    def get(self,request):
        cliente_dic = []
        cliente = Queries(Cliente).q_all()
        for i in cliente:
            if Suscripcion.objects.filter(cliente=i).count() > 0:
                cliente_dic.append(Clientes(i.nombre,i.id,Suscripcion.objects.filter(cliente=i).latest('dia_fin').dia_fin))
            else:
                cliente_dic.append(Clientes(i.nombre,i.id,0))
        # ordena lista de objetos
        cliente_dic.sort(key=attrgetter('vencimiento'))
        
        context = {
            'cliente':cliente_dic
        }   
        return render(request, 'cliente/listar.html', context)

class perfilCliente(View):
    def get(self,request,id):
        cliente = Cliente.objects.get(id=id)
        suscripciones = Suscripcion.objects.filter(cliente=cliente).order_by('-dia_fin')
        context = {
            'cliente':cliente,
            'suscripciones':suscripciones
        }
        return render(request,'cliente/perfil.html',context)


def agregarSuscripcion(request, id):
    dia_comienzo = datetime.date.today()
    dia_fin = datetime.datetime.now() + datetime.timedelta(30)
    cl = Queries(Cliente).q_get(id)
    susc = Queries(Suscripcion).q_filter(cl)
    hoy = datetime.date.today()
    if susc:
        last_suscripcion = susc.latest('dia_fin').dia_fin
        Suscripcion(cliente=cl,dia_comienzo=last_suscripcion,dia_fin=last_suscripcion+datetime.timedelta(31)).save()
    else:
        print("add new suscription")
        Suscripcion(cliente=cl,dia_comienzo=dia_comienzo,dia_fin=dia_fin).save()    
    # if hoy.getDate() > last_suscripcion.getDate() or hoy.getDate() == last_suscripcion.getDate():
    #     print("Se puede agregar mes", hoy, last_suscripcion)
    # else:
    #     print('No se puede agregar mes')

    # susc = Suscripcion(cliente=Cliente.objects.get(id=id),dia_comienzo=dia_comienzo,dia_fin=dia_fin)
    # susc.save()

    
    return redirect('apps.clientes:listar')

def removerSuscripcion(request,id):
    susc = Suscripcion.objects.get(id=id)
    susc.delete()
    print(id, "has been removed")
    return redirect('apps.clientes:listar')