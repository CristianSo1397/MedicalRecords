from django.shortcuts import render
from citas.models import Cita
from django.views import generic
from citas.forms import CitaForm
from django.urls import reverse_lazy
# Create your views here.
class ListarCitas(generic.ListView):
    model=Cita
    template_name="citas/listar_citas.html"
    context_object_name="obj"
class InsertarCita(generic.CreateView):
    model=Cita
    template_name="citas/insertar_cita.html"
    context_object_name="obj"
    form_class=CitaForm
    success_url=reverse_lazy("citas:citas_list")
class EditarCita(generic.UpdateView):
    model=Cita
    template_name="citas/insertar_cita.html"
    context_object_name="obj"
    form_class=CitaForm
    success_url=reverse_lazy("citas:citas_list")
class BorrarCita(generic.DeleteView):
    model=Cita
    template_name="citas/borrar_cita.html"
    context_object_name="obj"
    form_class=CitaForm
    success_url=reverse_lazy("citas:citas_list")

