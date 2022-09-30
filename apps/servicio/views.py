from django.shortcuts import render,redirect
from django.views import View
from .forms import FormServicio, FormPlan
from .queries import allServicio, idServicio
# Create your views here.

class ViewServicio(View):
    def get(self, request):
        form = FormServicio()
        servicios = allServicio()
        context = {
            'form':form,
            'servicios':servicios
        }
        return render(request,'servicio/add.html', context)
    def post(self, request):
        if request.method == 'POST':
            form = FormServicio(request.POST)
            if form.is_valid():
                form.save()
                return redirect('apps.servicio:add',)  

def MainServicio(request):
    servicios = allServicio()
    context = {
        'servicios':servicios
    }
    return render(request,'servicio/main.html', context)

def IdServicio(request,id):
    servicio = idServicio(id)
    context = {
        'servicio': servicio
    }
    return render(request, 'servicio/ver.html', context)

def addplan(request,id):
    servicio = idServicio(id)
    form = FormPlan()
    context = {
        'form':form,
        'servicio':servicio
    }
    return render(request, 'servicio/plan/add.html',context)