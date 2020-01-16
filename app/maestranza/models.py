from django.db import models
from django.contrib.auth.models import User


# Create your models here.
ESTADOS = (
    (0, 'Diseno'),
    (1, 'Materiales'),
    (2, 'Taller'),
    (3, 'Cnc'),
    (4, 'CorteHilo'),
    (5, 'Torno'),
)
ESTADO = (
    ('Diseno', 0),
    ('Materiales', 1),
    ('Taller', 2),
    ('Cnc', 3),
    ('CorteHilo', 4),
    ('Torno', 5),
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

class Estado(models.Model):
    # estados = models.IntegerField(choices=ESTADOS, default='0')
    # def __str__(self):  
    #     return '{}'.format(self.estados)
    estado = models.CharField(choices=ESTADO, verbose_name='estado', default='Diseno', max_length=100)
    def __str__(self):
        return '{}'.format(self.estado)
    

class Proyecto(models.Model):
    nombre_proyecto = models.CharField(max_length=50)
    empresa = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    persona = models.ManyToManyField(Persona, blank=True)
    prioridad = models.IntegerField(choices=PRIORIDAD, default=0)
    estado = models.ManyToManyField(Estado, blank=True)
    def __str__(self):
        return '{} {}'.format(self.nombre_proyecto, self.empresa)
