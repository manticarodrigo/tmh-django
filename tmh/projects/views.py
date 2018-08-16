from django.core import serializers
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Project
from .serializers import ProjectSerializer


class ListProject(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    @action(methods=['get'], detail=False, permission_classes=[])
    def me(self, request, pk=None):
        user = request.user
        serializer = ProjectSerializer(Project.objects.filter(user__pk=user.id), many=True)
        return Response(serializer.data)


class DetailProject(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer