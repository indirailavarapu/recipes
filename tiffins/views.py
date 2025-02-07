from django.shortcuts import render
from .models import *

# Create your views here.
def idly(request):
    i1=Idly.objects.all()
    return render(request,'tiffins/idly.html',{'i1':i1})

def dosa(request):
    d1=Dosa.objects.all()
    return render(request,'tiffins/dosa.html',{'d1':d1})

def vada(request):
    v1=Vada.objects.all()
    return render(request,'tiffins/vada.html',{'v1':v1})

def puri(request):
    p1=Puri.objects.all()
    return render(request,'tiffins/puri.html',{'p1':p1})

def chapati(request):
    c1=Chapati.objects.all()
    return render(request,'tiffins/chapati.html',{'c1':c1})

def parota(request):
    p1=Parota.objects.all()
    return render(request,'tiffins/parota.html',{'p1':p1})

def showIdly(request,id):
    idly=Idly.objects.get(id=id)
    return render(request,'tiffins/showIdly.html',{'idly':idly})

def showDosa(request,id):
    dosa=Dosa.objects.get(id=id)
    return render(request,'tiffins/showDosa.html',{'dosa':dosa})

def showVada(request,id):
    vada=Vada.objects.get(id=id)
    return render(request,'tiffins/showVada.html',{'vada':vada})

def showPuri(request,id):   
    puri=Puri.objects.get(id=id)
    return render(request,'tiffins/showPuri.html',{'puri':puri})

def showChapati(request,id):
    chapati=Chapati.objects.get(id=id)
    return render(request,'tiffins/showChapati.html',{'chapati':chapati})

def showParota(request,id):
    parota=Parota.objects.get(id=id)
    return render(request,'tiffins/showParota.html',{'parota':parota})
