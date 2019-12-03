from django.contrib import admin

from . import models

admin.site.register(models.BrandName)
admin.site.register(models.ModelNumber)
admin.site.register(models.Variant)