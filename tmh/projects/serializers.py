from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'id',
            'created_date',
            'modified_date',
            'start_date',
            'end_date',
            'style',
            'room_type',
            'video_url',
            'zipcode',
            'status',
            'designer_note',
            'final_note',
            'revision_count',
            'user'
        )