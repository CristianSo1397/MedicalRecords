from django import forms
from citas.models import Cita
class CitaForm(forms.ModelForm):
    class Meta: 
        model=Cita
        fields=['medico','especialidad','unidadAtencion','IDPaciente','fechaCita','horaCita']
        labels={'medico':'Medico','especialidad': 'Especialidad','unidadAtencion':'Unidad de Atencion ','IDPaciente':'ID del paciente',
        'fechaCita':'Fecha de la Cita', 'horaCita':'Hora'}
        widget={'medico': forms.TextInput()}

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })