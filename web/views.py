from django.shortcuts import render, get_object_or_404, HttpResponse
from . import models


def index(request):
    return render(request, 'index.html', {'services': models.Servicio.objects.all()})


def servicio(request, slug):
    obj = get_object_or_404(models.Servicio, slug=slug)
    return render(request, 'services.html', {'service': obj})


def subservicio(request, slug, subslug):
    parent = get_object_or_404(models.Servicio, slug=slug)
    obj = get_object_or_404(models.SubServicio, slug=subslug)

    return HttpResponse(obj.title)
