from django.shortcuts import render,redirect
from django.views import View
from apps.servicio.models import Plan
from django.views.generic import UpdateView
from .forms import FormServicio, FormPlan
from .queries import allServicio, idServicio, idPlan
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
    plan = Plan.objects.filter(servicio=servicio)
    context = {
        'servicio': servicio,
        'plan':plan
    }
    return render(request, 'servicio/ver.html', context)

def addplan(request,id):
    servicio = idServicio(id)
    form = FormPlan(request.POST)
    context = {
        'form':form,
        'servicio':servicio

    }
    
    if request.method == 'POST':
        if form.is_valid():
            aux = form.save(commit=False)
            aux.servicio = servicio
            aux.save()


    return render(request, 'servicio/plan/add.html',context)

class UpdatePlan(UpdateView):
    model = Plan
    form_class = FormPlan
    template_name=  'servicio/plan/edit.html'
    # fields = ['nombre','precio','descripcion']

