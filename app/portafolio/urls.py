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
from app.portafolio.views import portafolio, BlogList, BlogCreate
from django.contrib.auth.decorators import login_required


app_name = 'portfolio_app'
urlpatterns = [
    path('', portafolio, name="portfolio"),
    path('/blog/nuevo/',login_required(BlogCreate.as_view()), name='portafolio_crear'),
    path('blog/listar', login_required(BlogList.as_view()), name = 'portafolio_listar'),
]
