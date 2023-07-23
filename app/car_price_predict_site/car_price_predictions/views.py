from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import loader
import pickle as pkl
import pandas as pd
import os
import uuid
import datetime

from .models import Car, User

with open(f'{os.getcwd()}/../../models/full_pipeline_regressor.pkl', 'rb') as f:
    model = pkl.load(f)

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def prediction_form(request):
    return render(request, 'entering_data/prediction_form.html')

@login_required
def calculate_price(request):

    car_view = Car(request.POST)
    car_view.ID = uuid.uuid4()
    car_view.USER_ID = request.user.id

    form_dictionary = {key: request.POST.get(key, None) for key in Car.ColumnNames.column_names() \
                       if key not in ('id', 'user_id', 'price') and not key.startswith('__')}

    x = pd.DataFrame({key: [value] for key, value in form_dictionary.items()})
    predictions = model.predict(x)[0]

    car_view.PRICE = predictions

    for key, value in model.items():
        if key in Car.ColumnNames.numeric_column_names():
            try:
                car_view.__dict__[key.upper()] = float(value)
            except:
                car_view.__dict__[key.upper()] = value.encode()
        
        car_view.__dict__[key.upper()] = value.encode()
    
    for key, value in car_view.__dict__.items():
        print(f'{key}: {value}')

    car_view.save()

    return HttpResponse(f"{predictions}")


def register_view(request):
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