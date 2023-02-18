from django.forms import ModelForm, widgets,DateInput

from trabajador.models import Trabajador

class FormTrabajador(ModelForm):
    class Meta:
        model = Trabajador
        fields ='__all__'
        widgets={
            'fecha_de_nacimiento': DateInput(attrs={'type':'date'}),
            'fecha_contrato': DateInput(attrs={'type':'date'}),
            'fecha_finalizacion': DateInput(attrs={'type':'date'})
        }
