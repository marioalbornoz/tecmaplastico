from django.db import models
from django.contrib.auth.models import User


# Create your models here.
ESTADO = (
    ('Diseno', 'diseno'),
    ('Materiales','Materiales'),
    ('Taller','Taller'),
    ('Cnc','Cnc'),
    ('CorteHilo','CorteHilo'),
    ('Torno','Torno')
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
