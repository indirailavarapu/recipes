from django.shortcuts import render
from .models import *

# Create your views here.
def soups(request):
    s1=Soups.objects.all()
    return render(request,'veg/soups.html',{'s1':s1})

def curries(request):
    c1=Curries.objects.all()
    return render(request,'veg/curries.html',{'c1':c1})

def vegbiryani(request):
    v1=VegBiryani.objects.all()
    return render(request,'veg/vegbiryani.html',{'v1':v1})

def fastfood(request):  
    f1=FastFood.objects.all()
    return render(request,'veg/fastfood.html',{'f1':f1})  

def starters(request): 
    s1=Starters.objects.all()
    return render(request,'veg/starters.html',{'s1':s1})

def stirfry(request):
    s1=StirFry.objects.all()
    return render(request,'veg/stirfry.html',{'s1':s1})

def quickandeasy(request):
    q1=QuickAndEasy.objects.all()
    return render(request,'veg/quickandeasy.html',{'q1':q1})

def showSoups(request,id):
    soups=Soups.objects.get(id=id)
    return render(request,'veg/showSoups.html',{'soups':soups})

def showCurries(request,id):
    curries=Curries.objects.get(id=id)
    return render(request,'veg/showCurries.html',{'curries':curries})

def showVegBiryani(request,id):
    vegbiryani=VegBiryani.objects.get(id=id)
    return render(request,'veg/showVegbiryani.html',{'vegbiryani':vegbiryani})

def showFastFood(request,id):
    fastfood=FastFood.objects.get(id=id)
    return render(request,'veg/showFastfood.html',{'fastfood':fastfood})

def showStarters(request,id):
    starters=Starters.objects.get(id=id)
    return render(request,'veg/showStarters.html',{'starters':starters})

def showStirFry(request,id):
    stirfry=StirFry.objects.get(id=id)
    return render(request,'veg/showStirfry.html',{'stirfry':stirfry})

def showQuickAndEasy(request,id):
    quickandeasy=QuickAndEasy.objects.get(id=id)
    return render(request,'veg/showQuick.html',{'quickandeasy':quickandeasy})
