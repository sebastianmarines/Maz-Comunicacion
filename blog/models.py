from django.db import models

import storage_backends


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    featured_image = models.ImageField(storage=storage_backends.PublicMediaStorage(), null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
