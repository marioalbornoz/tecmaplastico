from django.shortcuts import render
from django.views.generic import ListView, DeleteView, CreateView
from django.urls import reverse_lazy
from app.portafolio.forms import BlogForm
from app.portafolio.models import Posteos

# Create your views here.

def portafolio(request):
    return render(request, 'base/base.html')

class BlogList(ListView):
    model = Posteos
    template_name = 'portafolio/portafolio_list.html'
    ordering = ['id']
    paginate_by = 5

class BlogCreate(CreateView):
    model = Posteos
    form_class = BlogForm
    template_name = 'portafolio/portafolio_forms.html'
    success_url = reverse_lazy('portfolio_app:portfolio_listar')
