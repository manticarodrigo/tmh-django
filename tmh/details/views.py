from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from tmh.projects.models import Project

from .models import ProjectDetail
from .permissions import IsEditorOrReadOnly
from .serializers import ProjectDetailSerializer

# Create your views here.
class ProjectDetailViewSet(viewsets.ModelViewSet):
    """
    Retrieves projects detail
    """
    queryset = ProjectDetail.objects.all()
    serializer_class = ProjectDetailSerializer
    permission_classes = (IsEditorOrReadOnly,)

    @action(methods=['get'], detail=False, permission_classes=[IsEditorOrReadOnly,])
    def project(self, request, pk=None):
        project_id = request.query_params['project']
        project = Project.objects.get(id=project_id)
        serializer = ProjectDetailSerializer(ProjectDetail.objects.filter(project__pk=project.id), many=True)
        return Response(serializer.data)