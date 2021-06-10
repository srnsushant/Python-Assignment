from rest_framework import serializers
from .models import RouterDetails

class RouterDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=RouterDetails
        fields=['hostname']
