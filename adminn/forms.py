from django.forms import *
from trabajador.models import *


class FormEmpresa(ModelForm):

    class Meta:
        model = Empresa
        fields ='__all__'
        widgets={ 
            'nombre': TextInput(attrs={'placeholder':'Escribe nombre..'}),
            'razon_social': TextInput(attrs={'placeholder':'Escribe razon social..'}),
            'direccion': TextInput(attrs={'placeholder':'Escribe direcciom..'}),
            'correro_electonico': TextInput(attrs={'placeholder':'Escribe Correo electronico..'}),
            'telefono': TextInput(attrs={'placeholder':'Escribe numero de telefono..'}),
        }

class FormSolicitud(ModelForm):
    class Meta:
        model = Solicitud
        fields ='__all__'
        widgets={ 
            'fecha_inicio': DateInput(attrs={'type':'date'}),
            'fecha_expiracion': DateInput(attrs={'type':'date'})
        }

