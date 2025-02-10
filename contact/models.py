from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=12)
    description=models.TextField()
    
    
    def __str__(self):
        return self.name
    
    # admin panel model name ContactUss to Contact Us
    class Meta:
         verbose_name_plural = "Contact Us"
    
    


