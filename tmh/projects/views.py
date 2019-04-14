from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Project
from .permissions import IsEditorOrReadOnly
from .serializers import ProjectSerializer, ProjectReadableSerializer


class ProjectViewSet(viewsets.ViewSet):
    """
    Retrieves projects
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsEditorOrReadOnly,)

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

    def partial_update(self, request, pk=None):
        project = Project.objects.get(id=pk)
        serializer = ProjectSerializer(project, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        project = Project.objects.get(id=pk)
        project.delete()
        return Response({})

    @action(methods=['get'], detail=False, permission_classes=[IsEditorOrReadOnly,])
    def me(self, request, pk=None):
        user = request.user
        project = Project.objects.filter(client__pk=user.id)
        serializer = ProjectReadableSerializer(project, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False, permission_classes=[IsEditorOrReadOnly,])
    def latest(self, request, pk=None):
        project = Project.objects.latest('modified_date')
        serializer = ProjectReadableSerializer(project)
        return Response(serializer.data)