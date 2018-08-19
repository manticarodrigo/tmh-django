from rest_framework import serializers
from .models import Project

from tmh.users.serializers import UserSerializer


class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = '__all__'

    created_date = serializers.DateTimeField(read_only=True)
    room = serializers.ChoiceField(choices=Project.ROOM_CHOICES)
    status = serializers.ChoiceField(choices=Project.STATUS_CHOICES)
    shared_with = serializers.ChoiceField(choices=Project.SHARED_WITH_CHOICES)
    budget = serializers.ChoiceField(choices=Project.BUDGET_CHOICES)

class ProjectReadableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'

    created_date = serializers.DateTimeField(read_only=True)
    room = serializers.CharField(source='get_room_display')
    status = serializers.ChoiceField(choices=Project.STATUS_CHOICES)
    shared_with = serializers.CharField(source='get_shared_with_display')
    budget = serializers.CharField(source='get_budget_display')
    client = UserSerializer()
    designer = UserSerializer()
