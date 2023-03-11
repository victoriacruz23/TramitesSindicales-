from django.forms import ModelForm, widgets,DateInput
from trabajador.models import Persona

class FormTrabajador(ModelForm):
    class Meta:
        model = Persona
        exclude = ['usuario', 'tipo_rol']
        widgets={ 
            'fecha_validacion': DateInput(attrs={'type':'date'}),
        }
