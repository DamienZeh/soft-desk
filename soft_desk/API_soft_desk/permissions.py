from rest_framework.permissions import BasePermission
from .models import Projects, Contributors


class IsAuthorAuthenticated(BasePermission):
    def has_object_permission(self, request, view, obj):
        # anyone authenticated, can create a project
        if request.method == "POST":
            return True

        elif Contributors.objects.filter(
            user_id=request.user.id,
            project_id=obj.id,
        ).exists():
            # Read a project for all contributors.
            if request.method == "GET":
                return True

            # CRUD permissions for author.
            elif Contributors.objects.filter(
                user_id=request.user.id,
                project_id=obj.id,
                role="auteur",
                permission="total",
            ).exists():
                return True
            else:
                return False
        else:
            return False


class IsContributorAuthenticated(BasePermission):
    def has_object_permission(self, request, view, obj):
        # new project allowed if user is registered

        if (
            Contributors.objects.filter(
                user_id=request.user.id,
                project_id=obj.id,
                role="collaborateur",
                permission="read",
            ).exists()
            and request.method == "GET"
        ):
            return True

            # CRUD permissions for author.
        elif Contributors.objects.filter(
            user_id=request.user.id,
            project_id=obj.id,
            role="auteur",
            permission="total",
        ).exists():
            return True
        else:
            return False
