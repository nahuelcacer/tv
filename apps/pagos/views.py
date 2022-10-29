from django.shortcuts import redirect
from multiprocessing import context
from django.shortcuts import render
from apps.periodo.models import Periodo
from .forms import addPago
from django.views import View
from apps.clientes.models import Cliente
from apps.pagos.models import Pagos
from django.db.models import Q


# Create your views here.
class ListarPagos(View):
    def get(self,request,id,periodo):
        cliente = Cliente.objects.get(id=id)
        n_periodo = Periodo.objects.get(nombre=periodo)
        pagos = Pagos.objects.filter(cliente=cliente, periodo=n_periodo)
        context = {
            'cliente':cliente,
            'periodo':n_periodo,
            'pagos':pagos   
            }
        return render(request, 'pago/listar.html', context)
    
class Pago(View):
    def get(self,request,id):
        cliente  = Cliente.objects.get(id=id)
        pagos = Pagos.objects.filter(~Q(saldo=0),cliente=cliente)
        for i in pagos:
            print(i.periodo)
        form = addPago()
        context = {
            'form':form
        }
        return render(request,'pago/addpay.html', context)

    def post(self,request,id):
        cliente = Cliente.objects.get(id=id)
        form = addPago(request.POST)
        def pay (importe,plan):
            saldo = plan - importe 
            return saldo 
        if request.method == "POST":
            if form.is_valid():
                aux = form.save(commit=False)
                aux.cliente = cliente
                pagos = Pagos.objects.filter(cliente=cliente, periodo=aux.periodo)
                if len(pagos) == 0:
                    saldo = pay(aux.importe, cliente.plan.precio)
                    if saldo == 0 or saldo > 0:
                        aux.saldo = saldo
                        aux.save()
                    else:
                        redirect(cliente)
                else:
                    saldo = pay(aux.importe, pagos.last().saldo)
                    if saldo == 0 or saldo > 0:
                        aux.saldo = saldo
                        aux.save()
                    else: 
                        redirect(cliente)
                    
                    
            
        return redirect(cliente)

        




