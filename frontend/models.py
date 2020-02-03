from django.db import models
import storage_backends


class Banner(models.Model):
    header = models.CharField(max_length=100, default="MAZ Comunicación")
    sub_header = models.CharField(max_length=200, default="Estrategia y Publicidad")
    image = models.ImageField(storage=storage_backends.PublicMediaStorage())

    def __str__(self):
        return "Configuración de banner"

    class Meta:
        verbose_name = "Configuración de banner"
        verbose_name_plural = "Configuración de banner"


class About(models.Model):
    description = models.TextField()

    def __str__(self):
        return "Acerca de MAZ"

    class Meta:
        verbose_name = "Acerca de MAZ"
        verbose_name_plural = "Acerca de MAZ"


class Servicios(models.Model):
    background_image = models.ImageField(storage=storage_backends.PublicMediaStorage())

    def __str__(self):
        return "Configuración de servicios"

    class Meta:
        verbose_name = "Configuración de servicios"
        verbose_name_plural = "Configuración de servicios"
