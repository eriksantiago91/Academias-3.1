from django.contrib import admin

# Register your models here.
from .models import Centros, Provincias, Cantones, Parroquias, Clases, Sectores, Tipos, Farmacias, Entidades


admin.site.register(Centros)
admin.site.register(Provincias)
admin.site.register(Cantones)
admin.site.register(Parroquias)
admin.site.register(Clases)
admin.site.register(Sectores)
admin.site.register(Tipos)
admin.site.register(Farmacias)
admin.site.register(Entidades)
