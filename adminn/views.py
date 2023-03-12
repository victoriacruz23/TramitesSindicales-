from django.shortcuts import render, redirect
from adminn.forms import *
from django.contrib.auth.decorators import login_required
from trabajador.models import *
# Create your views here.


@login_required
def createEmpersa(request):
    if request.method == "GET":
        formempresa = FormEmpresa()
    else:
        formempresa = FormEmpresa(request.POST)
        if formempresa.is_valid():
            formempresa.save()
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
