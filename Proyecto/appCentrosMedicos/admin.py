from django.contrib import admin

# Register your models here.
from .models import Cantones, Centros, Clases, Entidades, Farmacias, Parroquias,Provincias, Sectores, Tipos


admin.site.register(Cantones)
admin.site.register(Centros)
admin.site.register(Clases)
admin.site.register(Entidades)
admin.site.register(Farmacias)
admin.site.register(Parroquias)
admin.site.register(Provincias)
admin.site.register(Sectores)
admin.site.register(Tipos)
