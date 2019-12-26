from django import forms
from app.maestranza.models import Proyecto, Persona

class ProyectoForm(forms.ModelForm):

    class Meta:
        model = Proyecto

        fields = [
            'nombre_proyecto',
            'empresa',
            'fecha_inicio',
            'persona',
        ]
        labels = {
            'nombre_proyecto' : 'Nombre del proyecto',
            'empresa' : 'Empresa',
            'fecha_inicio' : 'Fecha de inicio',
            'persona' : 'Personal encargado',
        }
        widget = {
            'nombre_proyecto' : forms.TextInput(attrs={'class':'form-control'}),
            'empresa' : forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_inicio' : forms.TextInput(attrs={'class': 'form-control'}),
			'persona': forms.Select(attrs={'class':'form-control'}),

        }