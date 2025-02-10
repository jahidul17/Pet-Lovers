from django.contrib import admin
from .import models
# Register your models here.

class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',),}
    
    
class OriginAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('origin_country',),}
    
    
admin.site.register(models.Categories,CategoriesAdmin)
admin.site.register(models.Origin,OriginAdmin)

