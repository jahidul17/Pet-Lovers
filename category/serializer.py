from rest_framework import serializers
from .import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Categories
        fields='__all__'
        

class OriginSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Origin
        fields='__all__'
        
        

