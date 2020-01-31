from django import template
from web.models import Servicio

register = template.Library()

@register.simple_tag
def get_services_list():
    services = Servicio.objects.all()
    return services

