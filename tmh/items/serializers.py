from rest_framework import serializers
from .models import ProjectItem

class ProjectItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProjectItem
        fields = '__all__'

    status = serializers.ChoiceField(choices=ProjectItem.STATUS_CHOICES)