from django.db import models
from django.contrib.auth.models import User


# Create your models here.
ESTADOS = (
    (0, 'Asignado'),
    (1, 'trabajando'),
    (2, 'terminado'),
)
PRIORIDAD = (
    (0, 'Baja'),
    (1, 'Media'),
    (2, 'Alta'),
)
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    telefono = models.CharField(max_length=12)
    correo = models.EmailField()
    foto = models.ImageField(upload_to='profile', null=True, blank=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, default=True)


    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellidos)


class Proyecto(models.Model):
    nombre_proyecto = models.CharField(max_length=50)
    empresa = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    #persona = models.ForeignKey(
    #    Persona, null=True, blank=True, on_delete=models.CASCADE)
    persona = models.ManyToManyField(Persona, blank=True)
    estado = models.IntegerField(choices=ESTADOS, default=0)
    prioridad = models.IntegerField(choices=PRIORIDAD, default=0)
    def __str__(self):
        return '{} {}'.format(self.nombre_proyecto, self.empresa)
