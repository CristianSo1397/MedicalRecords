from django import forms
from pacientes.models import Paciente
class PacienteForm(forms.ModelForm):
    class Meta: 
        model=Paciente
        fields=['nombre','edad','ciudad','EPS']
        labels={'nombre':'Nombre del paciente', 'Edad':'Edad','Ciudad':'Ciudad','EPS':'EPS'}
        widget={'nombre': forms.TextInput()}

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })