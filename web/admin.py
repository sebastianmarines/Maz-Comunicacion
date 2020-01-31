from django.contrib import admin
from . import models


class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(models.Servicio, ServiceAdmin)
admin.site.register(models.SubServicio, ServiceAdmin)
