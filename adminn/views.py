from django.shortcuts import render, redirect
from adminn.forms import *
from django.contrib.auth.decorators import login_required
from trabajador.models import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.


@login_required
def createEmpersa(request):
    if request.method == "GET":
        formempresa = FormEmpresa()
    else:
        formempresa = FormEmpresa(request.POST)
        if formempresa.is_valid():
            formempresa.save()
            messages.success(request, f"Empresa creada satisfactoriamente")
            return redirect('consultaempresa')
        else:
            formempresa = FormEmpresa(request.POST)
    return render(request, 'admin/registroempresas.html', {'formempresa': formempresa})


@login_required
def consultaEmpresa(request):
    consultaEpresa = Empresa.objects.filter()
    return render(request, 'admin/consultaempresa.html', {'empresas': consultaEpresa})


@login_required
def registroSolicitud(request):
    formSolicitud = FormSolicitud()
    return render(request, 'admin/formSolicitud.html', {'formSolicitud': formSolicitud})


@login_required
def consultaTrabajador(request):
    # dato= get_object_or_404(Trabajador)
    dato = Persona.objects.filter().order_by('-id')
    return render(request, 'admin/consultaPersona.html', {'datos': dato})


@login_required
def createTrabajador(request):
    if request.method == "GET":
        form = UserCreationForm
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            contulataUser = User.objects.latest('id')
            idUser = contulataUser.id
            infUser = User.objects.get(pk=idUser)
            infTipo = Rol.objects.get(pk=2)
            instperfil = Persona()
            instperfil.usuario = infUser
            instperfil.tipo_rol = infTipo
            instperfil.save()
            return redirect('consultatrabajador')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

    return render(request, 'admin/registroTrabajador.html', {'form': form})
