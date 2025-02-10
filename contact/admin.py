from django.contrib import admin
from .import models
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display=['name','phone','description']

admin.site.register(models.ContactUs,ContactAdmin)
