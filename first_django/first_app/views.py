from django.shortcuts import render
from django.http import HttpResponse
from . import forms

def index(request):
    return render(request,'first_app\index.html')

def FormView(request):
    form= forms.SignUpForm()
    if request.method =="POST":
        form= forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)

    return render(request,"first_app/formpage.html",{"form":form})

def LoginView(request):
    Login = False
    form = forms.LoginForm()
    if request.method =="POST":
        form= forms.LoginForm(request.POST)
        if form.is_valid():
            Login = True
    return render(request,"first_app/loginpage.html",{"form":form,"Login":Login})