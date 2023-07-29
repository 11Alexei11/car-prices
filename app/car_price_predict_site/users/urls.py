from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login-form/", views.base_login_view, name='login-form'),
    path("registration-form/", views.base_register_view, name='registration-form'),
    path("registration-form/registrate/", views.registrate_user_view, name='registrate')
    # path("calculate_price/", views.calculate_price, name="calculate_price")
]