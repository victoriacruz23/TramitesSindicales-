from django.forms import *
from trabajador.models import *


class FormEmpresa(ModelForm):
    class Meta:
        model = Empresa
        fields ='__all__'
