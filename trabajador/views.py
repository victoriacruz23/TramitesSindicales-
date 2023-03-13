from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from trabajador.forms import FormPerfil
from trabajador.models import Trabajador, Persona

# Create your views here.


@login_required
def editarPerfil(request):
    datosPersona = Persona.objects.get(usuario=request.user.id)
    idPersona = datosPersona.id
    datosForm = get_object_or_404(Persona, pk=idPersona)
    if request.method == 'POST':
        form = FormPerfil(request.POST,request.FILES, instance=datosForm)
        if form.is_valid():
            form.save()
            messages.success(request, f"Guardado Correctamente")
            return redirect('editarperfil')
        else:
            form = FormPerfil(request.POST, instance=datosForm)
    else:
        form = FormPerfil(instance=datosForm)
    return render(request, 'trabajador/editarPerfil.html', {'form': form})


# no si sirvem
def perfil(request):
    if request.method == 'POST':
        form = FormPerfil(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consultatrabajador')
        else:
            form = FormPerfil(request.POST)

    else:
        form = FormPerfil()
    return render(request, 'perfil.html', {'form': form})


def inicio(request):
    return render(request, "usuario.html")


def editar(request, editar):
    trabajador_editar = get_object_or_404(Trabajador, pk=editar)
    if request.method == "GET":
        form = FormPerfil(instance=trabajador_editar)

    else:
        form = FormPerfil(request.POST, instance=trabajador_editar)
        if form.is_valid():
            form.save()
            return redirect('consultatrabajador')
        else:
            form = FormPerfil(request.POST, instance=trabajador_editar)

    return render(request, 'editar.html', {'editar': form})


def eliminar(request, eliminacion):
    trabajador_eliminar = get_object_or_404(Trabajador, pk=eliminacion)
    if request.method == "POST":
        trabajador_eliminar.delete()
        return redirect("consultatrabajador")


def credencial(request):
    if request.method == 'POST':
        form = FormPerfil(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consultatrabajador')
        else:
            form = FormPerfil(request.POST)

    else:
        form = FormPerfil()
    return render(request, 'credencial.html', {'form': form})


def remision(request):
    if request.method == 'POST':
        form = FormPerfil(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consultatrabajador')
        else:
            form = FormPerfil(request.POST)

    else:
        form = FormPerfil()
    return render(request, 'remision.html', {'form': form})


def pago(request):
    if request.method == 'POST':
        form = FormPerfil(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consultatrabajador')
        else:
            form = FormPerfil(request.POST)

    else:
        form = FormPerfil()
    return render(request, 'pago.html', {'form': form})
