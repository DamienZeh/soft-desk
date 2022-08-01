from tkinter.tix import Tree
from rest_framework.permissions import BasePermission
from .models import Projects, Contributors
from django.db.models import Q
from rest_framework.exceptions import ValidationError


class IsAuthorOrUserAuthenticated(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "GET" or request.method == "POST":
            return True
        elif request.method in ["PUT", "DELETE"]:
            if request.user == obj.author_user_id:
                return True


class IsContributorNotAuthorAuthenticated(BasePermission):
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
            error_message = f"this project doesn't exist."
            raise ValidationError(error_message) 


class IsContributorAuthorAuthenticated(BasePermission):
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
            error_message = f"this project doesn't exist."
            raise ValidationError(error_message) 

class IsAuthorIssueAuthenticated(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "GET" or request.method == "POST":
            return True
        elif request.method in ["PUT", "DELETE"]:
            if request.user == obj.assignee_user_id:
                return True

class IsAuthorCommentAuthenticated(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "GET" or request.method == "POST":
            return True
        elif request.method in ["PUT", "DELETE"]:
            if request.user == obj.author_user_id:
                return True




