from rest_framework.permissions import BasePermission
from .models import Projects


class IsAuthorOrUserAuthenticated(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return True
        elif request.method in ["POST", "PUT", "DELETE"]:
            return request.user == obj.author_user_id


class IsContributorNotAuthorAuthenticated(BasePermission):
    def has_permission(self, request, view):
       
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


class IsContributorAuthorAuthenticated(BasePermission):
    def has_permission(self, request, view):        
        if "project_pk" in view.kwargs:
            project = view.kwargs.get("project_pk")
        project_id = Projects.objects.get(pk=project)
        if request.user == project_id.author_user_id:
            return True
        else:
            return False
