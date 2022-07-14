import email
from urllib import response
from django.shortcuts import render, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login

# Create your views here.


def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, "index.html")
    # return HttpResponse("this is homepage")


def about(request):
    return render(request, "about.html")
    # return HttpResponse("this is about page")


def services(request):
    return render(request, "services.html")
    # return HttpResponse("this is services page")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone,
                          desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')

    return render(request, "contact.html")
    # return HttpResponse("this is contact page")


def loginUser(request):
    if request.method == "POST":
        # check if user has entered correct credetials
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, "login.html")

    return render(request, "login.html")


def logoutUser(request):
    logout(request)
    return redirect("/login")
