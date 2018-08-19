from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from tmh.projects.models import Project

from .models import ProjectItem
from .permissions import IsEditorOrReadOnly
from .serializers import ProjectItemSerializer

# Create your views here.
class ProjectItemViewSet(viewsets.ModelViewSet):
    """
    Retrieves and modifies project items
    """
    queryset = ProjectItem.objects.all()
    serializer_class = ProjectItemSerializer
    permission_classes = (IsEditorOrReadOnly,)

    @action(methods=['get'], detail=False, permission_classes=[IsEditorOrReadOnly,])
    def project(self, request, pk=None):
        project_id = request.query_params['project']
        project = Project.objects.get(id=project_id)
        serializer = ProjectItemSerializer(ProjectItem.objects.filter(project__pk=project.id), many=True)
        return Response(serializer.data)