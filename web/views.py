from django.shortcuts import render, get_object_or_404, HttpResponse
from django.core.mail import EmailMessage

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

            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            phone = form.cleaned_data.get("phone")
            city = form.cleaned_data.get("city")
            message = form.cleaned_data.get("message")

            subject = name + " envio un mensaje"

            new_message = f"""
            Nombre: {name}
            Correo: {email}
            Telefono: {phone}
            Ciudad: {city}
            Mensaje:
            {message}
            """

            mail = EmailMessage(subject, new_message, email, ['sebastian0marines@gmail.com'], reply_to=[email])
            mail.send()

        else:
            context['errors'] = True

    return render(request, 'contact.html', context)
