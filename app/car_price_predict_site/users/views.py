from django.shortcuts import render, redirect, HttpResponse
from .models import User


# Create your views here.

def index(request):
    return redirect('login-form')

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
            user.save()
            print('new user')
            return redirect('login-form')
        else:
            print('existing user')
            return redirect('registration-form')
    else:
        print(request.GET)
        raise Exception('this requesregister_statust should be post')