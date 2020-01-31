from django.shortcuts import render, get_object_or_404
from . import models


def index(request):
    return render(request, 'index.html', {'services': models.Servicio.objects.all()})


def servicio(request, slug):
    obj = get_object_or_404(models.Servicio, slug=slug)
    return render(request, 'services.html', {'service': obj})
