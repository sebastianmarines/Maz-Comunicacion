from django.contrib import admin
from . import models


class PortadasAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category')
    list_filter = ('category',)


admin.site.register(models.PortadasYColumnas, PortadasAdmin)
