from multiprocessing import context
from django.shortcuts import render



def Index(request):
    
        
    return render(request,'index.html')
