from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def hola(request):

    if request.method == "GET":
        form = UserCreationForm
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuariosesion = form.save()
            login(request, usuariosesion)
            return redirect('inicio')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

    return render(request, 'registro.html', {'form': form})

@login_required
def inicio(request):
    return render(request, 'inicio.html')


def inicio_sesion(request):

    if request.method == "GET":
        form = AuthenticationForm
    else:
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            password_usuario = form.cleaned_data.get("password")
            # from django.contrib.auth import authenticate
            # autenticacion por medio de la funcion authenticate
            user = authenticate(username=nombre_usuario,
                                password=password_usuario)
            if user is not None:
                # datos necesarios para el login
                login(request, user)
                messages.success(
                    request, f"Bienvenido al sistema {nombre_usuario}")
                return redirect("inicio")
            else:
                for msg in form.error_messages:
                    messages.error(request, form.error_messages[msg])
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

    return render(request, 'iniciosesion.html', {'form': form})


def cerrar_sesion(request):
    logout(request)
    return redirect('iniciosesion')
