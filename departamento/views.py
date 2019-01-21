from django.shortcuts import render
from django.http import HttpResponse
from . models import Camisa

def home(request):
    return render(request, 'home.html' ,{})

def camisa_list(request):
    camisas = Camisa.objects.all()
    return render(request, 'camisa/list.html', {'camisas':camisas})

def camisa_show(request, camisa_id):
    camisa = Camisa.objects.get(pk=camisa_id)
    return render(request, 'camisa/show.html', {'camisa':camisa})  

# Create your views here.
