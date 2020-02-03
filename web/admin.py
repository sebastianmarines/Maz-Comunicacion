from django.contrib import admin
from . import models


class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class SubServiceAdmin(ServiceAdmin):
    list_display = ("title", "parent")
    list_filter = ("parent",)


admin.site.register(models.Servicio, ServiceAdmin)
admin.site.register(models.SubServicio, SubServiceAdmin)
