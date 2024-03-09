from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import ReservacionForm
from django.contrib.auth.decorators import login_required
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
            
def iniciarSecion(request):
    if request.method=="GET":
        return render(request,"login.html",{
            "form":AuthenticationForm,
        }) 
    else:
        try:
            user=authenticate(request,
                            username=request.POST['username'],password=request.POST['password'])   
            if user is not None:
                login(request,user)
                return redirect("/")
            else:
                return render(request,"login.html",{
                "form":AuthenticationForm,
                "msg": "el usuario o contraseña es incorrecto/no existe"
            }) 
        except Exception as e:
            return render(request,"login.html",{
                "form":AuthenticationForm,
                "msg": f"Error{e}"
            }) 
def cerrarsesion(request):
    logout(request)
    return redirect("/")
@login_required
def nuevaReservacion(request):
    if request.method=="GET":
        return render(request,"nuevareservacion.html",{
                    "form":ReservacionForm,
                }) 
    else:
        try:
            form=ReservacionForm(request.POST)
            if form.is_valid():
                nuevo=form.save(commit=False) 
                if request.user.is_authenticated:
                    nuevo.usuario=request.user
                    nuevo.save()
                    return redirect("/")
                else:
                    return render(request,"nuevareservacion.html",{
                            "form":ReservacionForm,
                            "msg":"debe de autenticarse"
                    })
           
            else:
                return render(request,"nuevareservacion.html",{
                        "form":ReservacionForm,
                        "msg":"este formulario no es valido"
                })
                
        except Exception as e:
            return render(request,"nuevareservacion.html",{
                        "form":ReservacionForm,
                        "msg":f"Huboo un error{e}"
                })