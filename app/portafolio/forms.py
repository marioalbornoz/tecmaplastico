from django import forms
from app.portafolio. models import Posteos

class BlogForm(forms.ModelForm):
    class Meta:
        model = Posteos

        fields = [
            'title',
            'image',
            'description',

        ]
        labels = {
            'title' : 'Titulo',
            'image' : 'Imagen',
            'description' : 'Descripcion',

        }
        widget = {
        'Titulo' : forms.TextInput(attrs={'class':'form-control'}),
        'Imagen': forms.ImageField(),
        'description' : forms.TextInput(attrs={'class':'form-control'}),
        }
