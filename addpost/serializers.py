from rest_framework import serializers
from .import models


class PostSerializers(serializers.ModelSerializer):
    #show name alter id
    category = serializers.StringRelatedField( many=False)
    origin = serializers.StringRelatedField( many=False)
    class Meta:
        model=models.Post
        fields='__all__'


class ReviewerSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.Reviewer
        fields='__all__'
    
    
