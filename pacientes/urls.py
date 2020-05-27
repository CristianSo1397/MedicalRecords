from django.urls import path
from pacientes.views import ListarPacientes, InsertarPaciente, EditarPaciente, BorrarPaciente

urlpatterns=[
    path('pacientes', ListarPacientes.as_view(), name='pacientes_list'),
    path('pacientes/new', InsertarPaciente.as_view(), name='insertar_paciente'),
    path('pacientes/edit<int:pk>', EditarPaciente.as_view(), name='editar_paciente'),
    path('pacientes/delete<int:pk>', BorrarPaciente.as_view(), name='borrar_paciente'),
]