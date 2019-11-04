from django.urls import path
from app.produccion.views import index_produccion

app_name = 'produccion_app'

urlpatterns = [
    path('', index_produccion, name="produccion"),
]
