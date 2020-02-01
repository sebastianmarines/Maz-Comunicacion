from django.shortcuts import render, get_object_or_404

from .models import PortadasYColumnas


def portadas_list(request):
    objs = PortadasYColumnas.objects.filter(category=1)
    context = {
        'title': "Portadas y Columnas",
        'mexico': False,
        'periodicos': objs
    }

    return render(request, 'portadas-y-columnas.html', context)


def portada(request, slug):
    queryset = PortadasYColumnas.objects.filter(category=1)
    obj = get_object_or_404(queryset, slug=slug)

    return render(request, 'periodico.html', {'periodico': obj})


def portadas_list_mexico(request):
    objs = PortadasYColumnas.objects.filter(category=2)
    context = {
        'title': "Portadas y Columnas de México",
        'mexico': True,
        'periodicos': objs
    }

    return render(request, 'portadas-y-columnas.html', context)


def portada_mexico(request, slug):
    queryset = PortadasYColumnas.objects.filter(category=2)
    obj = get_object_or_404(queryset, slug=slug)

    return render(request, 'periodico.html', {'periodico': obj})
