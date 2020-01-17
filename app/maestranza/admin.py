from django.contrib import admin
from app.maestranza.models import Persona, Proyecto, Estados

# Register your models here.
admin.site.register(Persona)
admin.site.register(Proyecto)
admin.site.register(Estados)