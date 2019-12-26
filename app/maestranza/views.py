from django.shortcuts import render
from app.maestranza.models import Proyecto, Persona
from django.views.generic import ListView
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'maestranza/index.html');

class ProyectList(ListView):
    model = Proyecto
    template_name = 'maestranza/proyect_list.html'
    ordering = ['id']
    paginate_by = 3