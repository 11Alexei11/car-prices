from django.shortcuts import render, HttpResponse
from .models import User

import datetime

# Create your views here.

def index(request):
    return HttpResponse("Hello")

def base_register_view(request):
    return render(request, 'users/register_form.html')

def registrate_user_view(request):
    if request.POST:
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']

        if not User.objects.filter(name=name, surname=surname, email=email).exists():
            user = User(
                name=name,
                surname=surname,
                email=email,
                registration_date=datetime.datetime.now()
            )
            user.save()