from rest_framework import serializers
from tmh.core.models.project import Project
from tmh.core.models.item import ProjectItem

class ProjectItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProjectItem
        fields = '__all__'

    status = serializers.ChoiceField(choices=ProjectItem.STATUS_CHOICES)