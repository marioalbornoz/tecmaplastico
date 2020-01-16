from django.contrib import admin
from app.maestranza.models import Persona, Proyecto, Estado

# Register your models here.
admin.site.register(Persona)
admin.site.register(Estado)
admin.site.register(Proyecto)