from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    sub_coah = models.BooleanField()
    sub_nl = models.BooleanField()
    sub_mex = models.BooleanField()
    message = models.TextField()
