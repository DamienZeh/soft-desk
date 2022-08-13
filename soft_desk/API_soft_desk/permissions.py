from rest_framework.permissions import BasePermission
from .models import Projects
from rest_framework.exceptions import ValidationError


class IsAuthorAuthenticated(BasePermission):
    """
    Check if is author or not.
    Allows update or delete if he's author,
     and read if he's only contributor,
     and post if just user.
    """

    def has_object_permission(self, request, view, obj):
        if request.method == "GET" or request.method == "POST":
            return True
        elif request.method in ["PUT", "DELETE"]:
            if request.user == obj.author_user_id:
                return True


class IsContributorAuthenticated(BasePermission):
    """
    Check if is a contributor of this project,
    and if project exists.
    """

    def has_permission(self, request, view):
        try:
            if "project_pk" in view.kwargs:
                project = view.kwargs.get("project_pk")
            else:
                return True
            project_id = Projects.objects.get(pk=project)
            contributors = project_id.contributor.all()
            if request.user in contributors:
                return True
            else:
                return False
        except Projects.DoesNotExist:
            error_message = "this project doesn't exist."
            raise ValidationError(error_message)


class IsContributorAuthorAuthenticated(BasePermission):
    """
    Check if user is the author of this project,
    and if project exists.
    """

    def has_permission(self, request, view):
        try:
            if "project_pk" in view.kwargs:
                project = view.kwargs.get("project_pk")
            project_id = Projects.objects.get(pk=project)
            if request.user == project_id.author_user_id:
                return True
            else:
                return False
        except Projects.DoesNotExist:
            error_message = "this project doesn't exist."
            raise ValidationError(error_message)
