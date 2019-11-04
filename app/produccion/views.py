from django.shortcuts import render

# Create your views here.

def index_produccion(request):
    return render(request, 'produccion/produccion_index.html')