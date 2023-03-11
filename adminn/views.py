from django.shortcuts import render, redirect
from adminn.forms import *
from trabajador.models import *
# Create your views here.


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


def consultaEmpresa(request):
    consultaEpresa = Empresa.objects.filter()
    return render(request, 'admin/consultaempresa.html', {'empresas': consultaEpresa})

def registroSolicitud(request):
    formSolicitud = FormSolicitud()
    return render(request,'admin/formSolicitud.html',{'formSolicitud':formSolicitud})
