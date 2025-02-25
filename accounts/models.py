from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class ImageUpload(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=CloudinaryField('accounts/images/')
    mobile_no=models.CharField(max_length=12)
    
    class Meta:
        verbose_name_plural = "ImageUpload"
    
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
    

