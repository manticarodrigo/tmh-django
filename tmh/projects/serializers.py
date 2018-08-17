from rest_framework import serializers
from .models import Project, User
from tmh.users.serializers import UserSerializer


class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = '__all__'

    created_date = serializers.DateTimeField(read_only=True)
    room = serializers.ChoiceField(choices=Project.ROOM_CHOICES)
    status = serializers.ChoiceField(choices=Project.STATUS_CHOICES)
    user = UserSerializer()