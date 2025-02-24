from django.db import models
from category.models import Categories,Origin
from django import forms
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

COLOUR_CHOICES =( 
    ("Black", "BLACK"), 
    ("White", "WHITE"), 
    ("Brown", "BROWN"), 
    ("Gray", "GRAY"), 
    ("Red", "RED"),
    ("Tabby", "TABBY"), 
    ("Tortoiseshell", "TORTOISESHELL"), 
    ("Calico", "CALICO"), 
     
) 

GENDER_CHOICES=(
    ("Male","MALE"),
    ("Female","FEMALE"),
)

class Post(models.Model):
    category=models.ForeignKey(Categories,on_delete=models.CASCADE)
    origin=models.ForeignKey(Origin,on_delete=models.CASCADE)
    colour=models.CharField(choices=COLOUR_CHOICES, max_length=20,blank=True,null=True)
    title=models.CharField(max_length=100,blank=True)
    image=CloudinaryField("addpost/images",blank=True,null=True)
    price=models.IntegerField()
    gender=models.CharField(choices=GENDER_CHOICES,max_length=20,null=True)
    contact=models.CharField(max_length=12)
    description=models.TextField()
    age=models.CharField(max_length=20)
    
    # def __str__(self):
    #     return f"{self.category} {self.image}"
        
    
    
    
STAR_CHOICES={
    ('⭐','⭐'),
    ('⭐⭐','⭐⭐'),
    ('⭐⭐⭐','⭐⭐⭐'),
    ('⭐⭐⭐⭐','⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐'),
    
}

class Reviewer(models.Model):
    reviewer=models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    rating=models.CharField(choices=STAR_CHOICES,max_length=10)
    
    
    def __str__(self):
        return f" Reviewer : {self.reviewer.first_name}"
    

    

