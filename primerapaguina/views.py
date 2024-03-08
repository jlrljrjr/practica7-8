from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout
# Create your views here.

def holamundo(request):
    return HttpResponse("hola mundo")

def home(request):
    return render(request,"home.html")

def registro(request):
    if request.method =='GET':
        return render(request,"registro.html",{
            "form":UserCreationForm
    })
    else:
        req=request.POST
        if req['password1']==req['password2']:
            try:
                user= User.objects.create_user(
                username=req['username'],
                password=req['password1']
                ) 
                user.save()
                login(request,user)
                return redirect('/')
            except IntegrityError as ie:
                return render(request,"registro.html",{
                "form":UserCreationForm,
                "msg":"ya existe este nombre de usuario"
            })
            except Exception as e:
                                return render(request,"registro.html",{
                "form":UserCreationForm,
                "msg":f"se a encontrado el sig error {e}"
            })

        else:
            return render(request,"registro.html",{
                "form":UserCreationForm,
                "msg":"favor de verificar sus contraseñas"
            })
def cerrarsesion(request):
    return logout(request)
