from django.urls import path
from citas.views import ListarCitas, InsertarCita, EditarCita, BorrarCita

urlpatterns=[
    path('citas', ListarCitas.as_view(), name='citas_list'),
    path('citas/new', InsertarCita.as_view(), name='insertar_cita'),
    path('citas/edit<int:pk>', EditarCita.as_view(), name='editar_cita'),
    path('citas/delete<int:pk>', BorrarCita.as_view(), name='borrar_cita'),
]