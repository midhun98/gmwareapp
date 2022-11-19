from django.contrib import admin
from .import models

# Register your models here.
admin.site.register(models.MarketPlace)
admin.site.register(models.ZipCode)
admin.site.register(models.Brand)

