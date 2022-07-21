from re import M
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Projects
from .serializers import ProjectSerializer


class ProjectViewSet(ModelViewSet):
    permission_class = IsAuthenticated
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Projects.objects.filter(author_user_id=self.request.user.pk)

    def perform_create(self, serializer):
        serializer.save(author_user_id=self.request.user.pk)
