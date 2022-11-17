from django.contrib import admin
from django.urls import path
from first_app import views

app_name="first_app"

urlpatterns = [
    path("sign_up/",views.FormView,name="Sign_up"),
    path("login/",views.LoginView,name="Login")
]