from django.shortcuts import render, HttpResponse
from django.template import loader
import pickle as pkl
import pandas as pd
import json
import os

from .models import Car

with open(f'{os.getcwd()}/../../models/full_pipeline_regressor.pkl', 'rb') as f:
    model = pkl.load(f)

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def prediction_form(request):
    return render(request, 'entering_data/prediction_form.html')

def calculate_price(request):
    form_dictionary = {key: request.POST.get(key, None) for key in Car.ColumnNames.column_names() \
                       if key not in ('id', 'user_id', 'price') and not key.startswith('__')}

    x = pd.DataFrame({key: [value] for key, value in form_dictionary.items()})

    predictions = model.predict(x)[0]

    return HttpResponse(f"{predictions}")