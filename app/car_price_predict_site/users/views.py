from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User

import datetime

# Create your views here.

def index(request):
    return render(request, 'users/login_form.html')

def base_register_view(request):
    return render(request, 'users/register_form.html')

def base_login_view(request):
    return render(request, 'users/login_form.html')

def registrate_user_view(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        if not User.objects.filter(NAME=name, EMAIL=email, PASSWORD=password).exists():
            user = User(
                NAME=name,
                EMAIL=email,
                PASSWORD=password
            )
            # user.save()
            messages.success(request=request, message="You have registrated succesfully")
        else:
            messages.error(request=request, message="This user has already registered")

        return render(request, 'users/login_form.html')
    else:
        print(request.GET)
        raise Exception('this request should be post')