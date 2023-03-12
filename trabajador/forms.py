from django.forms import ModelForm, widgets,DateInput
from trabajador.models import Persona

class FormPerfil(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs.update({'autocomplete': 'off','class': 'form-control'})
    class Meta:
        model = Persona
        exclude = ['usuario', 'tipo_rol']
        widgets={ 
            'fecha_nacimiento': DateInput(attrs={'type':'date'}),
            'fecha_validacion': DateInput(attrs={'type':'date'}),
        }
