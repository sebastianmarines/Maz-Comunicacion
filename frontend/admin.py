from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from . import models


class AboutModelAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


admin.site.register(models.Banner)
admin.site.register(models.About, AboutModelAdmin)
