from rest_framework import serializers
from .models import *

class ProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project 
        fields = '__all__'