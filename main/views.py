from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from django.urls import reverse

# Create your views here.

def home(request):
    l1 = Latest.objects.all()
    t1 = Trending.objects.all()
    return render(request, 'home.html', {'l1': l1, 't1': t1})  

def showLatest(request,id):
    latest=Latest.objects.get(id=id)
    return render(request,'main/showLatest.html',{'latest':latest})

def showTrending(request,id):
    trending=Trending.objects.get(id=id)
    return render(request,'main/showTrending.html',{'trending':trending})

def veg(request):
    return render(request,'main/veg.html')

def nonveg(request):
    return render(request,'main/nonveg.html')

def desserts(request):
    return render(request,'main/desserts.html')

def snacks(request):
    return render(request,'main/snacks.html')

def drinks(request):
    return render(request,'main/drinks.html')

def tiffins(request):
    return render(request,'main/tiffins.html')

def calories(request):
    return render(request,'main/calories.html')


def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('main:signup')


        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Signup successful! Please log in.")
        return redirect('main:login')

    return render(request, 'main/signup.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        if not username or not password:
            messages.error(request, "Username and password are required!")
            return redirect('main:login')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect(reverse('main:home')) 
        else:
            messages.error(request, "Invalid credentials!")
            return redirect('main:login')

    return render(request, 'main/login.html')


def logout_view(request):
    logout(request)
    return redirect('main:login')
