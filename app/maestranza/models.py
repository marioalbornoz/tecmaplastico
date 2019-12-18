from django.db import models

# Create your models here.


class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    telefono = models.CharField(max_length=12)
    correo = models.EmailField()

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellidos)


class Proyecto(models.Model):
    nombre_proyecto = models.CharField(max_length=50)
    empresa = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    #persona = models.ForeignKey(
    #    Persona, null=True, blank=True, on_delete=models.CASCADE)
    persona = models.ManyToManyField(Persona, blank=True)

    def __str__(self):
        return '{} {}'.format(self.nombre_proyecto, self.empresa)
