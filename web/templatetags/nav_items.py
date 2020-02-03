from django import template
from django.urls import reverse
from web.models import Servicio

register = template.Library()

@register.simple_tag
def get_services_list():
    services = Servicio.objects.all()
    return services

@register.simple_tag
def service_url():
    path = reverse('web:index') + '#servicios'
    return path

