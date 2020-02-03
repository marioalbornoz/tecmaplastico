"""proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from app.maestranza.views import index, ProyectList, ProyectDelete, ProyectCreate, area, cardList, ProyectUpdate
from django.contrib.auth.decorators import login_required

app_name = 'maestranza_app'
urlpatterns = [
    path('', login_required(index), name="index"),
    path('areas/', login_required(area), name='area'),
    path('areas/card', login_required(cardList.as_view()), name='card'),
    path('nuevo/',login_required(ProyectCreate.as_view()), name='proyecto_crear'),
    path('listar/', login_required(ProyectList.as_view()), name = 'proyecto_listar'),
    path( '<int:pk>/eliminar/', ProyectDelete.as_view(), name='proyecto_eliminar'),
    path('<int:pk>/editar/', ProyectUpdate.as_view(), name='proyecto_editar')
]
