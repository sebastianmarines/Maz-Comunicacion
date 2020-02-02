from django.shortcuts import render, get_object_or_404, HttpResponse

from . import models
from blog.models import Post
from .forms import ContactForm


def index(request):
    return render(request, 'index.html', {'services': models.Servicio.objects.all(), 'post_list':Post.objects.filter(status=1).order_by('-created_on')[:5]})


def servicio(request, slug):
    obj = get_object_or_404(models.Servicio, slug=slug)
    return render(request, 'services.html', {'service': obj})


def subservicio(request, slug, subslug):
    parent = get_object_or_404(models.Servicio, slug=slug)
    obj = get_object_or_404(models.SubServicio, slug=subslug)

    return HttpResponse(obj.title)


def contact(request):
    context = {'form': ContactForm()}
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            context['sucess'] = True
        else:
            context['errors'] = True

    return render(request, 'contact.html', context)
