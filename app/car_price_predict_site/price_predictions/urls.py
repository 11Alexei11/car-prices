from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("prediction-form/", views.prediction_form, name='prediction-form'),
    path("calc-price/", views.calculate_price, name="calc-price")
]