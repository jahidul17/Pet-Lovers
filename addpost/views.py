from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serializers
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticatedOrReadOnly ]
    
    queryset=models.Post.objects.all()
    serializer_class=serializers.PostSerializers


class ReviewerViewSet(viewsets.ModelViewSet):    
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticatedOrReadOnly ]
    
    queryset=models.Reviewer.objects.all()
    serializer_class=serializers.ReviewerSerializers

