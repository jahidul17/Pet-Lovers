from rest_framework import serializers
from .import models

#For convert jason data
class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.ContactUs
        fields='__all__'
        


