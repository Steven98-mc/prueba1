from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        x=auth.authenticate(username=username,password=password)
        if x is None:
            messages.success(request, 'USUARIO O CONTRASEÑA INCORRECTO')
            return redirect("/")
        else:
            return redirect('home page')
    else:
        return render(request, 'login.html')