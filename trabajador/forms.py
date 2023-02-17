from django.forms import ModelForm
from trabajador.models import Trabajador
class FormTrabajador(ModelForm):
    class Meta:
        model = Trabajador
        fields = '__all__'

