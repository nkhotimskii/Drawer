from rest_framework import viewsets
from rest_framework.response import Response

from drawer import serializers
from .models import Plan, Project


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = serializers.ProjectSerializer


class PlanViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows plans to be viewed or edited.
    """
    queryset = Plan.objects.all()
    serializer_class = serializers.PlanSerializer


class ProjectWithPlansViewSet(viewsets.ViewSet):
    """
    API endpoint that allows all projects with plans
    to be viewed.
    """

    def list(self, request):
        projects = Project.objects.prefetch_related('plans').all()
        serializer = serializers.ProjectWithPlansSerializer(
            projects,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)