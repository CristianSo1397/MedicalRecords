from django.db import models

# Create your models here.
class Cita(models.Model):
    horaCita=models.TimeField()
    fechaCita=models.DateField()
    medico=models.CharField(max_length=100,)
    especialidad=models.CharField(max_length=100,)
    unidadAtencion=models.CharField(max_length=100,)
    IDPaciente=models.CharField(max_length=100,)
    def __str__(self):
        return '{}'.format(self.medico)
    def save(self):
        super(Cita, self).save()

    class Meta:
        verbose_name_plural="Citas"