from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.conf import settings
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from .models import Projects, Contributors
from django.db.models import Q
from .serializers import (
    ProjectListSerializer,
    ProjectDetailSerializer,
    ContributorDetailSerializer,
    ContributorListSerializer,
)
from .permissions import (
    IsAuthorOrUserAuthenticated,
    IsContributorNotAuthorAuthenticated,
    IsContributorAuthorAuthenticated,
)


class ProjectViewSet(ModelViewSet):
    permission_classes = [
        IsAuthenticated,
        IsAuthorOrUserAuthenticated,
        IsContributorNotAuthorAuthenticated,
    ]
    serializer_class = ProjectDetailSerializer

    def get_queryset(self):
        return Projects.objects.filter(contributor=self.request.user)

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
    permission_classes = [
        IsAuthenticated,
        IsContributorNotAuthorAuthenticated,
        IsContributorAuthorAuthenticated,
    ]
    serializer_class = ContributorDetailSerializer

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
            error_message = f"you're not contributor of this project."
            raise ValidationError(error_message)

    def get_permissions(self):
        if (
            self.request.method == "POST"
            or self.request.method == "DELETE"
            or self.request.method == "PUT"
        ):
            permission_classes = [
                IsAuthenticated,
                IsContributorAuthorAuthenticated,
            ]
        else:
            permission_classes = [
                IsAuthenticated,
                IsContributorNotAuthorAuthenticated,
            ]
        return [permission() for permission in permission_classes]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ContributorListSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        # Get project_id and linked project to contributor
        target_user_id = self.request.data["user_id"]
        project = get_object_or_404(Projects, id=self.kwargs["project_pk"])

        if Contributors.objects.filter(
            project_id=project, user_id=target_user_id
        ).exists():
            error_message = f"user {target_user_id} is already contributor of project {project}."
            raise ValidationError(error_message)
        else:
            serializer.save(project_id=project)

    def destroy(self, request, *args, **kwargs):
        if Contributors.objects.get(pk=kwargs["pk"]).user_id == request.user:
            error_message = {"message": "You cannot delete yourself."}
            raise ValidationError(error_message)
        return super().destroy(request, *args, **kwargs)
