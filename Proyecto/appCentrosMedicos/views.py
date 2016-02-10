from django.shortcuts import render
from django.shortcuts import render_to_response
from appCentrosMedicos.models import Centros

# Create your views here.

def lista_centros(request):
    centros = Centros.objects.all()
    return render_to_response('lista_centros.html', {'listaCentros':centros})
