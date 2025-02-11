from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from django.core.mail import send_mail
from django.conf import settings

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
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        # Check if the user already exists
        if User.objects.filter(email=email).exists():
            return redirect('main:login')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken. Please choose another one.")
            return redirect("main:signup")  # Redirect back to the signup page
        
        # Create new user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # 📩 Send Confirmation Email to User
        user_subject = "Welcome to Our Platform!"
        user_message = f"Hi {username},\n\nThank you for registering!\n\nBest Regards,\nTeam"
        send_mail(user_subject, user_message, settings.EMAIL_HOST_USER, [email], fail_silently=False)

        # 📩 Send Admin Notification with User Details
        admin_subject = "New User Registration"
        admin_message = f"New user registered:\n\nUsername: {username}\nEmail: {email}\nPassword: {password}"
        send_mail(admin_subject, admin_message, settings.EMAIL_HOST_USER, ['nandinikamireddy11@gmail.com'], fail_silently=False)

        return redirect('main:login')

    return render(request, 'main/signup.html')




def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main:home')  # Change to your homepage
        else:
            messages.error(request, "Invalid credentials!")
            return redirect('main:login')

    return render(request, 'main/login.html')


def logout_view(request):
    logout(request)
    return redirect('main:login')