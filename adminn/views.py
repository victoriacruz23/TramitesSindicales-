from django.shortcuts import render,redirect
from adminn.forms import *
# Create your views here.
def createEmpersa(request):
    if request.method == "GET":
       formempresa  = FormEmpresa()
    else:
        formempresa = FormEmpresa(request.POST)
        if formempresa.is_valid():
            formempresa.save()
            return redirect('consultatrabajador')
        else:
            formempresa = FormEmpresa(request.POST)
    return render(request,'admin/registroempresas.html',{'formempresa':formempresa})