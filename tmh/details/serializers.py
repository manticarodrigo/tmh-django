from rest_framework import serializers
from .models import ProjectDetail

class ProjectDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProjectDetail
        fields = '__all__'

    created_date = serializers.DateTimeField(read_only=True)
    type = serializers.ChoiceField(choices=ProjectDetail.TYPE_CHOICES)