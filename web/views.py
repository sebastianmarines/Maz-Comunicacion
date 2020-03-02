from django.shortcuts import render, get_object_or_404, HttpResponse
from django.core.mail import EmailMessage
from django.conf import settings

from . import models
from frontend.models import Banner, About
from blog.models import Post
from periodicos.models import Configuracion as NewsConfig
from .forms import ContactForm
from contact.models import Contact


def index(request):
    return render(request, 'index.html', {
        'services': models.Servicio.objects.all(),
        'post_list': Post.objects.filter(status=1).order_by('-created_on')[:5],
        'banner': Banner.objects.get(pk=1),
        'about': About.objects.get(pk=1),
        'periodicos': {
            'coahuila': NewsConfig.objects.get(title=1),
            'mexico': NewsConfig.objects.get(title=2),
            'nl': NewsConfig.objects.get(title=3)
        }
    })


def servicio(request, slug):
    obj = get_object_or_404(models.Servicio, slug=slug)
    return render(request, 'services.html', {'service': obj})


def subservicio(request, slug, subslug):
    parent = get_object_or_404(models.Servicio, slug=slug)
    obj = get_object_or_404(models.SubServicio, slug=subslug)

    return render(request, 'subservicio.html', {'parent': parent, 'service': obj})


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
            sub_coah =form.cleaned_data.get("sub_coahuila")
            sub_nl = form.cleaned_data.get("sub_nl")
            sub_mex = form.cleaned_data.get("sub_mexico")

            Contact.objects.create(name=name, email=email, phone=phone, city=city, sub_coah=sub_coah, sub_nl=sub_nl,
                                   sub_mex=sub_mex, message=message)

            coahuila = "✔️" if sub_coah else "❌"
            nl = "✔️" if sub_nl else "❌"
            mex = "✔️" if sub_mex else "❌"

            subject = name + " envió un mensaje"

            new_message = f"""
            Nombre: {name}
            Correo: {email}
            Telefono: {phone}
                Portadas Coahuila: {coahuila}
                Portadas Nuevo León: {nl}
                Portadas México: {mex}
            Ciudad: {city}
            Mensaje:
            {message}
            """

            mail = EmailMessage(subject, new_message, email, settings.EMAIL_RECEIVER, reply_to=[email])
            mail.send()

        else:
            context['errors'] = True

    return render(request, 'contact.html', context)


def politica_privacidad(request):
    return render(request, 'politica-privacidad.html')


def politica_cookies(request):
    return render(request, 'politica-cookies.html')
