from multiprocessing import context
from django.shortcuts import render
import os 


def Index(request):
    
        
    return render(request,'index.html')

def Serve(request):
    from django.views.static import serve
    filepath = 'static/tv_channels_raul1.m3u'
    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))