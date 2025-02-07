from django.shortcuts import render
from .models import *

# Create your views here.
def chicken(request):
    data=Chicken.objects.all()
    return render(request,'nonveg/chicken.html',{'data':data})

def seafood(request):
    data=Seafood.objects.all()
    return render(request,'nonveg/seafood.html',{'data':data})

def starters(request):
    data=Starters.objects.all()
    return render(request,'nonveg/starters.html',{'data':data}) 

def meat(request):
    data=Meat.objects.all()
    return render(request,'nonveg/meat.html',{'data':data})

def beef(request):
    data=Beef.objects.all()
    return render(request,'nonveg/beef.html',{'data':data})

def pork(request):
    data=Pork.objects.all()
    return render(request,'nonveg/pork.html',{'data':data})

def showChicken(request,id):
    chicken=Chicken.objects.get(id=id)
    return render(request,'nonveg/showChicken.html',{'chicken':chicken})

def showSeafood(request,id):
    seafood=Seafood.objects.get(id=id)
    return render(request,'nonveg/showSea.html',{'seafood':seafood})

def showStarters(request,id):
    starters=Starters.objects.get(id=id)
    return render(request,'nonveg/showStarters.html',{'starters':starters})

def showMeat(request,id):
    meat=Meat.objects.get(id=id)
    return render(request,'nonveg/showMeat.html',{'meat':meat})

def showBeef(request,id):
    beef=Beef.objects.get(id=id)
    return render(request,'nonveg/showBeef.html',{'beef':beef})

def showPork(request,id):
    pork=Pork.objects.get(id=id)
    return render(request,'nonveg/showPork.html',{'pork':pork})