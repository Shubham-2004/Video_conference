from django.shortcuts import render
from .forms import *

# Create your views here
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'login.html',{'success':"Registration Successful.Please Login"})
        else:
            error_message = form.errors.as_text()
            return render(request,'register.html', {'error': error_message})
    return render(request,"register.html")
def login(request):
    return render(request,"login.html")
