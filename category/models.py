from django.db import models

# Create your models here.
class Categories(models.Model):
    name=models.CharField(max_length=30)
    slug=models.SlugField(max_length=40)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"
    

class Origin(models.Model):
    origin_country=models.CharField(max_length=30)
    slug=models.SlugField(max_length=40)
    
    def __str__(self):
        return self.origin_country