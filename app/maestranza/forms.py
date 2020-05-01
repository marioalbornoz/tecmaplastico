from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from app.maestranza.models import Proyecto, Persona

class ProyectoForm(forms.ModelForm):
   
    class Meta:
        model = Proyecto

        fields = [
            'nombre_proyecto',
            'empresa',
            'fecha_inicio',
            'persona',
            'prioridad',
            'estados',
        ]
        labels = {
            'nombre_proyecto' : 'Nombre del proyecto',
            'empresa' : 'Empresa',
            'fecha_inicio' : 'Fecha de inicio',
            'persona' : 'Personal encargado',
            'prioridad' : 'Prioridad',
            'estados' : 'Estados',
        }
        
        widget = {
            'nombre_proyecto' : forms.TextInput(attrs={'class':'form-control'}),
            'empresa' : forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_inicio' : forms.DateTimeInput(format='%d/%m/%s', attrs={'class':'form-control','type':'date'}),
		 	'persona': forms.MultipleChoiceField(required=True),
            'prioridad': forms.CheckboxSelectMultiple(attrs={'class':'form-check'}),
            'estados' : forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple(attrs={'class':'checkbox'})),
        }

# ESTADOS = (
#     (0, 'Diseno'),
#     (1, 'Materiales'),
#     (2, 'Taller'),
#     (3, 'Cnc'),
#     (4, 'CorteHilo'),
#     (5, 'Torno'),
# )
# class AvanceForm(forms.Form):
#     estado = forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple, choices=ESTADOS)


class AddPeopleForm(forms.ModelForm):
    class Meta:
        model = Persona

        fields = [
            'nombre',
            'apellidos',
            'correo',
            'telefono',
            'foto',
            'usuario'
        ]
        labels = {
            'nombre' : 'Nombre',
            'apellidos' : 'Apellidos',
            'correo' : 'Correo',
            'telefono' : 'Telefono',
            'foto' : 'Foto de perfil',
            'usuario' : 'Usuarios',
        }
        widget = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control'}),
            'correo': forms.EmailInput(attrs={'class':'form-control'}),
            'telefono':forms.TextInput(attrs={'class':'form-control'}),
            'foto': forms.TextInput(attrs=None),
            'usuario':forms.TextInput(attrs=None)
        }