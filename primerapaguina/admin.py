from django.contrib import admin
from .models import Reservacion
# Register your models here.
class ResevacionAdmin(admin.ModelAdmin):
    readonly_fields=("fecha_creacion",)

admin.site.register(Reservacion,ResevacionAdmin)
