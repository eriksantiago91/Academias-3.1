from django.contrib import admin

# Register your models here.
from .models import centros, provincias, cantones, parroquias, clases, sectores, tipos, farmacias, entidades

admin.site.register(centros)
admin.site.register(provincias)
admin.site.register(cantones)
admin.site.register(parroquias)
admin.site.register(clases)
admin.site.register(sectores)
admin.site.register(tipos)
admin.site.register(farmacias)
admin.site.register(entidades)
