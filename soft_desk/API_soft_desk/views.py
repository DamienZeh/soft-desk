from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from .models import Projects, Contributors, Issues, Comments
from .serializers import (
    ProjectListSerializer,
    ProjectDetailSerializer,
    ContributorDetailSerializer,
    ContributorListSerializer,
    IssueDetailSerializer,
    IssueListSerializer,
    CommentListSerializer,
    CommentDetailSerializer,
)
from .permissions import (
    IsAuthorAuthenticated,
    IsContributorAuthenticated,
    IsContributorAuthorAuthenticated,
)


class ProjectViewSet(ModelViewSet):
    """
    Get CRUD for a project.
    Create if doesn't exist already with the same name.
    Read for contributors of this project(list or detail).
    Update if it's author of project.
    Delete if it's author of project.
    """

    permission_classes = [IsAuthenticated, IsAuthorAuthenticated]
    serializer_class = ProjectDetailSerializer

    def get_queryset(self):
        return Projects.objects.filter(contributor=self.request.user)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ProjectListSerializer(queryset, many=True)
        if len(queryset) < 1:
            error_message = "You are not contributor in a project."
            raise ValidationError(error_message)
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
    """
    Get CRUD for Contributors.
    Add/Create if user is not contributor already.
    Read contributors of this project(list or detail).
    Delete contributor if it's author of project who decide.
    Can't delete author himself.
    """

    serializer_class = ContributorDetailSerializer

    def get_queryset(self):
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
            error_message = "you're not contributor of this project."
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
                IsContributorAuthenticated,
            ]
        return [permission() for permission in permission_classes]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ContributorListSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):

        user_id = self.request.data["user_id"]
        project = get_object_or_404(Projects, id=self.kwargs["project_pk"])

        if Contributors.objects.filter(
            project_id=project, user_id=user_id
        ).exists():
            error_message = (
                f"user {user_id} is already contributor of project {project}."
            )
            raise ValidationError(error_message)
        else:
            serializer.save(project_id=project)

    def destroy(self, request, *args, **kwargs):
        if Contributors.objects.get(pk=kwargs["pk"]).user_id == request.user:
            error_message = {"message": "You cannot delete yourself."}
            raise ValidationError(error_message)
        return super().destroy(request, *args, **kwargs)


class IssueViewSet(ModelViewSet):
    """
    Get CRUD for a issue in a project.
    Create if doesn't exist already with the same name.
    Read for contributors of this project(list or detail).
    Update if it's author of issue.
    Delete if it's author of issue.
    """

    serializer_class = IssueDetailSerializer

    def get_queryset(self):
        try:
            contributor_exist = Contributors.objects.get(
                Q(project_id=self.kwargs["project_pk"])
                & Q(user_id=self.request.user)
            )
            if contributor_exist:
                return Issues.objects.filter(
                    project_id=self.kwargs["project_pk"]
                )
        except Contributors.DoesNotExist:
            error_message = "you're not contributor of this project."
            raise ValidationError(error_message)

    def get_permissions(self):
        if self.request.method == "POST":
            permission_classes = [
                IsAuthenticated,
                IsContributorAuthorAuthenticated,
                IsContributorAuthenticated,
            ]

        if self.request.method == "DELETE" or self.request.method == "PUT":
            permission_classes = [
                IsAuthenticated,
                IsAuthorAuthenticated,
            ]
        else:
            permission_classes = [
                IsAuthenticated,
                IsContributorAuthenticated,
            ]
        return [permission() for permission in permission_classes]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = IssueListSerializer(queryset, many=True)
        if len(queryset) < 1:
            error_message = "They are not issue in this project."
            raise ValidationError(error_message)
        return Response(serializer.data)

    def perform_create(self, serializer):
        project = get_object_or_404(Projects, id=self.kwargs["project_pk"])
        serializer.save(
            project_id=project,
            assignee_user_id=self.request.user,
            author_user_id=self.request.user,
        )


class CommentViewSet(ModelViewSet):
    """
    Get CRUD for a comment in an issue in a project.
    Create if doesn't exist already with the same description.
    Read for contributors of this project(list or detail).
    Update if it's author of comment.
    Delete if it's author of comment.
    """

    serializer_class = CommentDetailSerializer

    def get_queryset(self):
        try:
            contributor_exist = Contributors.objects.get(
                Q(project_id=self.kwargs["project_pk"])
                & Q(user_id=self.request.user)
            )
            if contributor_exist:
                return Comments.objects.filter(
                    issue_id=self.kwargs["issue_pk"]
                )
        except Contributors.DoesNotExist:
            error_message = "you're not contributor of this project."
            raise ValidationError(error_message)

    def get_permissions(self):
        if self.request.method == "POST":
            permission_classes = [
                IsAuthenticated,
                IsContributorAuthorAuthenticated,
                IsContributorAuthenticated,
            ]

        if self.request.method == "DELETE" or self.request.method == "PUT":
            permission_classes = [
                IsAuthenticated,
                IsAuthorAuthenticated,
            ]
        else:
            permission_classes = [
                IsAuthenticated,
                IsContributorAuthenticated,
            ]
        return [permission() for permission in permission_classes]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CommentListSerializer(queryset, many=True)
        if len(queryset) < 1:
            error_message = "They are not comment in this issue."
            raise ValidationError(error_message)
        return Response(serializer.data)

    def perform_create(self, serializer):
        issue = get_object_or_404(Issues, id=self.kwargs["issue_pk"])
        serializer.save(issue_id=issue, author_user_id=self.request.user)
