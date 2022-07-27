from django.shortcuts import render
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Projects, Contributors
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .serializers import (
    ProjectListSerializer,
    ProjectDetailSerializer,
    ContributorSerializer,
)
from .permissions import IsAuthorAuthenticated, IsContributorAuthenticated


class ProjectViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsAuthorAuthenticated]
    serializer_class = ProjectDetailSerializer

    def get_queryset(self):
        return Projects.objects.filter(author_user_id=self.request.user)

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


class ContributorsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsContributorAuthenticated]
    serializer_class = ContributorSerializer

    def get_queryset(self):
        # check if user is contributor
        try:
            contributor_exist = Contributors.objects.get(
                Q(project_id=self.kwargs["project_pk"])
                & Q(user_id=self.request.user)
            )
            if contributor_exist:
                return Contributors.objects.filter(
                    project_id=self.kwargs["project_pk"]
                )

        except Contributors.DoesNotExist:
            print("Vous n'êtes pas un contributeur du projet.")

    def perform_create(self, serializer):
        # Get project_id and linked project to contributor
        project = get_object_or_404(Projects, id=self.kwargs["project_pk"])
        serializer.save(project_id=project)
