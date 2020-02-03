from django.contrib import admin
from . import models


class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "sub_coah", "sub_nl", "sub_mex")
    list_filter = ("sub_coah", "sub_nl", "sub_mex")


admin.site.register(models.Contact, ContactAdmin)