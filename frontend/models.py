from django.db import models
import storage_backends


class Banner(models.Model):
    header = models.CharField(max_length=100, default="MAZ Comunicación")
    sub_header = models.CharField(max_length=200, default="Estrategia y Publicidad")
    image = models.ImageField(storage=storage_backends.PublicMediaStorage())

    def __str__(self):
        return "Banner configuration"

    class Meta:
        verbose_name = "Banner configuration"
        verbose_name_plural = "Banner configuration"
