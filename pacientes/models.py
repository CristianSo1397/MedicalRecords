from django.db import models

# Create your models here.
class Paciente(models.Model):
   
    nombre=models.CharField(max_length=100,)
    edad=models.CharField(max_length=100,)
    ciudad=models.CharField(max_length=100,)
    EPS=models.CharField(max_length=100,)
    def __str__(self):
        return '{}'.format(self.nombre)
    def save(self):
        super(Paciente, self).save()

    class Meta:
        verbose_name_plural="Pacientes"