from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from trabajador.forms import FormTrabajador
from trabajador.models import Trabajador,Persona

# Create your views here.
def inicio(request):
    return render(request, "usuario.html")

def create(request):
    datosPersona = Persona.objects.get(usuario = request.user.id)
    idPersona =  datosPersona.id
    datosForm = get_object_or_404(Persona,pk=idPersona)
    if request.method == 'POST':
        form = FormTrabajador(request.POST,instance=datosForm)
        if form.is_valid():
            form.save()
            messages.success(request, f"Guardado Correctamente")
            return redirect('createtrabajdor')
        else:
            form = FormTrabajador(request.POST,instance=datosForm)
    else:
        form = FormTrabajador(instance=datosForm)
    return render(request, 'trabajador/editartrabajador.html', {'form': form})


def consulta(request):
    # dato= get_object_or_404(Trabajador)
    dato = Trabajador.objects.all()
    return render(request, 'consulta.html', {'datos': dato})


def editar(request, editar):
    trabajador_editar = get_object_or_404(Trabajador, pk=editar)
    if request.method == "GET":
        form = FormTrabajador(instance=trabajador_editar)
        
    else:
        form = FormTrabajador(request.POST, instance=trabajador_editar)
        if form.is_valid():
            form.save()
            return redirect('consultatrabajador')
        else:
            form = FormTrabajador(request.POST, instance=trabajador_editar)

    return render(request, 'editar.html', {'editar': form})


def eliminar(request, eliminacion):
    trabajador_eliminar = get_object_or_404(Trabajador, pk=eliminacion)
    if request.method == "POST":
        trabajador_eliminar.delete()
        return redirect("consultatrabajador")
    
def credencial(request):
    if request.method == 'POST':
        form = FormTrabajador(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consultatrabajador')
        else:
            form = FormTrabajador(request.POST)

    else:
        form = FormTrabajador()
    return render(request, 'agregartrabajador.html', {'form': form})


def remision():
    form= FormTrabajador