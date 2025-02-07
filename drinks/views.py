from django.shortcuts import render
from .models import *

# Create your views here.
def milkshakes(request):
    m1=Milkshakes.objects.all()
    return render(request,'drinks/milkshakes.html',{'m1':m1})

def smoothies(request):
    s1=Smoothies.objects.all()
    return render(request,'drinks/smoothies.html',{'s1':s1})

def tea(request):
    t1=Tea.objects.all()
    return render(request,'drinks/tea.html',{'t1':t1})

def coffee(request):
    c1=Coffee.objects.all()
    return render(request,'drinks/coffee.html',{'c1':c1})

def juices(request):
    j1=Juices.objects.all()
    return render(request,'drinks/juices.html',{'j1':j1})

def showMilkshakes(request,id):
    milkshakes=Milkshakes.objects.get(id=id)
    return render(request,'drinks/showMilkshakes.html',{'milkshakes':milkshakes})

def showSmoothies(request,id):
    smoothies=Smoothies.objects.get(id=id)
    return render(request,'drinks/showSmoothies.html',{'smoothies':smoothies})

def showTea(request,id):
    tea=Tea.objects.get(id=id)
    return render(request,'drinks/showTea.html',{'tea':tea})

def showCoffee(request,id):
    coffee=Coffee.objects.get(id=id)
    return render(request,'drinks/showCoffee.html',{'coffee':coffee})

def showJuices(request,id):
    juices=Juices.objects.get(id=id)
    return render(request,'drinks/showJuices.html',{'juices':juices})

