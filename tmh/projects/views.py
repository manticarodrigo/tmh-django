from django.core import serializers
from rest_framework import viewsets, mixins, generics
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Project, ProjectDetail
from .permissions import IsUserOrReadOnly
from .serializers import ProjectSerializer, ProjectReadableSerializer, ProjectDetailSerializer


class ProjectViewSet(viewsets.ViewSet):
    """
    Retrieves projects
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsUserOrReadOnly,)

    def list(self, request):
        queryset = Project.objects.all()
        serializer = ProjectReadableSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        project = Project.objects.get(pk=pk)
        serializer = ProjectReadableSerializer(project)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProjectSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

    def update(self, request, pk=None):
        serializer = ProjectSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        user = Project.objects.get(id=pk)
        user.delete()
        return Response({})

    @action(methods=['get'], detail=False, permission_classes=[IsUserOrReadOnly,])
    def me(self, request, pk=None):
        user = request.user
        serializer = ProjectReadableSerializer(Project.objects.filter(user__pk=user.id), many=True)
        return Response(serializer.data)

class ProjectDetailViewSet(viewsets.ModelViewSet):
    """
    Retrieves projects detail
    """
    queryset = ProjectDetail.objects.all()
    serializer_class = ProjectDetailSerializer
    permission_classes = (IsUserOrReadOnly,)

    @action(methods=['get'], detail=False, permission_classes=[IsUserOrReadOnly,])
    def project(self, request, pk=None):
        project_id = request.query_params['project']
        project = Project.objects.get(id=project_id)
        serializer = ProjectDetailSerializer(ProjectDetail.objects.filter(project__pk=project.id), many=True)
        return Response(serializer.data)