from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from trabajador.forms import FormTrabajador
from trabajador.models import Trabajador

# Create your views here.


def create(request):
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


def consulta(request):
    # dato= get_object_or_404(Trabajador)
    dato = Trabajador.objects.all()
    return render(request, 'consulta.html', {'datos': dato})


def editar(request):
    form = FormTrabajador()
    return render(request, 'editar.html', {'form': form})


def eliminar(request, eliminacion):
    trabajador_eliminar = get_object_or_404(Trabajador, pk=eliminacion)
    if request.method == "POST":
        trabajador_eliminar.delete()
        return redirect("consultatrabajador")
