from django.urls import path
from app.produccion.views import index_produccion

urlpatterns = [
    path('', index_produccion, name="produccion"),
]
