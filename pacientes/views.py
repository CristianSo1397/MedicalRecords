from django.shortcuts import render
from  pacientes.models import Paciente
from django.views import generic
from pacientes.forms import PacienteForm
from django.urls import reverse_lazy

# Create your views here.
class ListarPacientes(generic.ListView):
    model=Paciente
    template_name="pacientes/listar_pacientes.html"
    context_object_name="obj"
class InsertarPaciente(generic.CreateView):
    model=Paciente
    template_name="pacientes/insertar_paciente.html"
    context_object_name="obj"
    form_class=PacienteForm
    success_url=reverse_lazy("pacientes:pacientes_list")
class EditarPaciente(generic.UpdateView):
    model=Paciente
    template_name="pacientes/editar_paciente.html"
    context_object_name="obj"
    form_class=PacienteForm
    success_url=reverse_lazy("pacientes:pacientes_list")
class BorrarPaciente(generic.DeleteView):
    model=Paciente
    template_name="pacientes/borrar_paciente.html"
    context_object_name="obj"
    form_class=PacienteForm
    success_url=reverse_lazy("pacientes:pacientes_list")


