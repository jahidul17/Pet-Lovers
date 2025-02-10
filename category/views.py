from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serializer
from rest_framework.views import APIView

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset=models.Categories.objects.all()
    serializer_class=serializer.CategorySerializer
    

class OriginViewSet(viewsets.ModelViewSet):
    queryset=models.Origin.objects.all()
    serializer_class=serializer.OriginSerializer
    
