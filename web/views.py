from django.shortcuts import render
from . import models

def index(request):
    return render(request, 'index.html', {'services': models.Servicio.objects.all()})