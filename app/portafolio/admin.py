from django.contrib import admin
from app.portafolio.models import Posteos

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Posteos, ProjectAdmin)
