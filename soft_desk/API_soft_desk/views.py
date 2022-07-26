from django.shortcuts import render
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Projects, Contributors

from .serializers import ProjectListSerializer, ProjectDetailSerializer
from .permissions import IsAuthorAuthenticated


class ProjectViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsAuthorAuthenticated]
    serializer_class = ProjectDetailSerializer

    def get_queryset(self):
        return Projects.objects.filter(
            author_user_id=self.request.user
        )  # et ou contributeur, à rajouter

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ProjectListSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        project = serializer.save(author_user_id=self.request.user)
        contributor = Contributors.objects.create(
            user_id=self.request.user,
            project_id=project,
            role="auteur",
            permission="total",
        )
        contributor.save()

    def perform_update(self, serializer, *args, **kwargs):
        serializer.save(author_user_id=self.request.user)

    def perform_delete(self, serializer, *args, **kwargs):
        serializer.save(author_user_id=self.request.user)

    """
    if user = author_user_id:
        alors on peut delete/update
    """


"""class RetrieveProjectDetails(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectDetailSerializer

    def get_queryset(self):
        return Projects.objects.get(author_user_id=self.request.user)"""
