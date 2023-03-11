from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from trabajador.models import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

# Create your views here.

def no_autenticado(user):
    return not user.is_authenticated


def vistasPruebas(request):
    return render(request, 'base.html')

@user_passes_test(no_autenticado, login_url='/trabajadores/create')
def hola(request):
    select = ""
    if request.method == "GET":
        form = UserCreationForm
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuariosesion = form.save()
            contulataUser = User.objects.latest('id')
            idUser = contulataUser.id
            infUser = User.objects.get(pk=idUser)
            infTipo = Rol.objects.get(pk=2)
            instperfil = Persona()
            instperfil.usuario = infUser
            instperfil.tipo_rol = infTipo
            instperfil.save()
            select = Persona.objects.filter(usuario=idUser)
            login(request, usuariosesion)
            # request.session.setdefault('how_many_visits', 0)
            # request.session['how_many_visits'] += 1
            return redirect('inicio')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

    return render(request, 'registro.html', {'form': form, 'select': select})


@login_required
def inicio(request):
    return render(request, 'inicio.html')

@user_passes_test(no_autenticado, login_url='/trabajadores/create')
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


