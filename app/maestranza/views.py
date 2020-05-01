from django.shortcuts import render
from app.maestranza.models import Proyecto, Persona
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from app.maestranza.forms import ProyectoForm, AddPeopleForm

# Create your views here.
def index(request):
    return render(request, 'maestranza/index.html')

def area(request):
	return render(request, 'maestranza/proyect_area.html')

class cardList(ListView):
	model = Proyecto
	template_name = 'maestranza/proyect_card.html'
	ordering = ['id']

def card(request):
	return render(request,'maestranza/proyect_card.html' )

class ProyectList(ListView):
    model = Proyecto
    template_name = 'maestranza/proyect_list.html'
    ordering = ['id']
    paginate_by = 4


class ProyectCreate(CreateView):
	model = Proyecto
	form_class = ProyectoForm
	template_name = 'maestranza/proyect_forms.html'
	success_url = reverse_lazy('maestranza_app:proyecto_listar')

class ProyectDelete(DeleteView):
	model = Proyecto
	template_name = 'maestranza/proyect_delete.html'
	success_url = reverse_lazy('maestranza_app:proyecto_listar')

class ProyectUpdate(UpdateView):
	model = Proyecto
	form_class = ProyectoForm
	template_name = 'maestranza/proyect_forms.html'
	success_url = reverse_lazy('maestranza_app:proyecto_listar')

class AddPeople(CreateView):
	model = Persona
	form_class = AddPeopleForm
	template_name = 'user/people_form.html'
	success_url = reverse_lazy('maestranza_app:proyecto_listar')

class ListPeople(ListView):
	model = Persona
	template_name = 'user/people_list.html'
	ordering = ['id']
	paginate_by = 20