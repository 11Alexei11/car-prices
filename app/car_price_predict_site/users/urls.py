from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login-form/registration-form/", views.base_register_view, name='registration-form'),
    path('login-form/', views.base_login_view, name='login-form')
    # path("calculate_price/", views.calculate_price, name="calculate_price")
]