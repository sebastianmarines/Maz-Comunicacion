from django.db import models
import storage_backends

PORTADAS = 1
PORTADASMEXICO = 2
PORTADASNL = 3
CATEGORY = (
    (PORTADAS, ('Portadas Coahuila')),
    (PORTADASMEXICO, ('Portadas México')),
    (PORTADASNL, ('Portadas Nuevo León'))
)


class PortadasYColumnas(models.Model):

    title = models.CharField(max_length=15)
    thumbnail = models.ImageField(storage=storage_backends.PublicMediaStorage(), blank=True)
    file = models.FileField(storage=storage_backends.NewsMediaStorage())
    slug = models.SlugField(blank=True)
    category = models.PositiveSmallIntegerField(
        choices=CATEGORY,
        default=PORTADAS
    )

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = "Portadas y Columnas"


class Configuracion(models.Model):
    title = models.PositiveSmallIntegerField(
        choices=CATEGORY,
        default=PORTADAS
    )
    image = models.ImageField(storage=storage_backends.PublicMediaStorage(), blank=True)

    def __str__(self):
        return self.title
