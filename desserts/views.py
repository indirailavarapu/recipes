from django.shortcuts import render
from .models import *

# Create your views here.
def cakes(request):
    c1=Cakes.objects.all()
    return render(request,'desserts/cakes.html',{'c1':c1})

def chocolate(request):
    c1=Chocolate.objects.all()
    return render(request,'desserts/chocolate.html',{'c1':c1})

def icecream(request):
    i1=IceCream.objects.all()
    return render(request,'desserts/icecream.html',{'i1':i1})

def fruits(request):
    f1=Fruits.objects.all()
    return render(request,'desserts/fruits.html',{'f1':f1})

def nuts(request):
    n1=Nuts.objects.all()
    return render(request,'desserts/nuts.html',{'n1':n1})

def cookies(request):
    c1=Cookies.objects.all()
    return render(request,'desserts/cookies.html',{'c1':c1})

def showCakes(request,id):
    cakes=Cakes.objects.get(id=id)
    return render(request,'desserts/showCakes.html',{'cakes':cakes})

def showChocolate(request,id):
    chocolate=Chocolate.objects.get(id=id)
    return render(request,'desserts/showChocolate.html',{'chocolate':chocolate})

def showIceCream(request,id):
    icecream=IceCream.objects.get(id=id)
    return render(request,'desserts/showIce.html',{'icecream':icecream})

def showFruits(request,id):
    fruits=Fruits.objects.get(id=id)
    return render(request,'desserts/showFruits.html',{'fruits':fruits})

def showNuts(request,id):
    nuts=Nuts.objects.get(id=id)
    return render(request,'desserts/showNuts.html',{'nuts':nuts})

def showCookies(request,id):
    cookies=Cookies.objects.get(id=id)
    return render(request,'desserts/showCookies.html',{'cookies':cookies})