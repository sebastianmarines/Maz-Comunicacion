from django.db import models
import storage_backends


class Servicio(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(storage=storage_backends.PublicMediaStorage(), blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class SubServicio(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField()
    image = models.ImageField(storage=storage_backends.PublicMediaStorage())
    parent = models.ForeignKey(Servicio, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
