from django.shortcuts import render
from .models import *

# Create your views here.
def traditional(request):
    t1=Traditional.objects.all()
    return render(request,'snacks/traditional.html',{'t1':t1})

def chips(request):
    c1=Chips.objects.all()
    return render(request,'snacks/chips.html',{'c1':c1})

def fries(request):
    f1=Fries.objects.all()
    return render(request,'snacks/fries.html',{'f1':f1})

def springrolls(request):
    s1=SpringRolls.objects.all()
    return render(request,'snacks/springrolls.html',{'s1':s1})

def showTraditional(request,id):
    traditional=Traditional.objects.get(id=id)
    return render(request,'snacks/showTraditional.html',{'traditional':traditional})

def showChips(request,id):  
    chips=Chips.objects.get(id=id)
    return render(request,'snacks/showChips.html',{'chips':chips})

def showFries(request,id):
    fries=Fries.objects.get(id=id)
    return render(request,'snacks/showFries.html',{'fries':fries})

def showSpringRolls(request,id):
    springrolls=SpringRolls.objects.get(id=id)
    return render(request,'snacks/showSpringrolls.html',{'springrolls':springrolls})
