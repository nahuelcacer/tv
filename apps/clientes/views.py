from datetime import date, datetime
from multiprocessing import context
from operator import attrgetter
from tokenize import group
from django.shortcuts import render, redirect
from django.views import View
from apps.clientes.models import Cliente
from apps.clientes.forms import formCliente
from apps.periodo.models import Periodo
from apps.pagos.models import Pagos
from django.db.models import Sum


# class Clientes():
#     """Crea objeto de clientes para enviar en el context"""
#     def __init__(self,nombre,id,vencimiento):
#         self.nombre = nombre
#         self.id = id
#         self.vencimiento = vencimiento


#     def faltan(self):
#         if self.vencimiento != 0:
#             venc = self.vencimiento - datetime.date.today()  
#             return int(venc.days)
#         else:
#             return "Sin suscripcion"
#     def p_vencimiento(self):
#         """Fecha transformada a str"""
#         if self.vencimiento != 0:
#             return self.vencimiento.strftime('%d/%m/%Y')
#         else: 
#             return ""

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
        cliente = Cliente.objects.all()
        
        # cliente_dic = []
        # cliente = Queries(Cliente).q_all()
        # for i in cliente:
        #     if Suscripcion.objects.filter(cliente=i).count() > 0:
        #         cliente_dic.append(Clientes(i.nombre,i.id,Suscripcion.objects.filter(cliente=i).latest('dia_fin').dia_fin))
        #     else:
        #         cliente_dic.append(Clientes(i.nombre,i.id,0))
        # # ordena lista de objetos
        # cliente_dic.sort(key=attrgetter('vencimiento'))
        
        context = {
            'cliente': cliente
        }   
        return render(request, 'cliente/listar.html', context)

class perfilCliente(View):
    def get(self,request,id):
        cliente = Cliente.objects.get(id=id)
        pagos = Pagos.objects.filter(cliente=cliente).select_related('periodo').order_by('-periodo')[:10]
        group_pay = pagos.values('periodo__nombre', 'periodo').annotate(Sum('importe'))
        for i in group_pay:
           saldo = cliente.plan.precio - i['importe__sum']
           i['saldo'] =  saldo
        context = {
            'cliente':cliente,
            'pagos':group_pay
        }
        return render(request,'cliente/perfil.html',context)


