from pyexpat import model
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Projects, Contributors, Issues


class ProjectDetailSerializer(serializers.ModelSerializer):
    def validate_title(self, value):
        if Projects.objects.filter(title=value).exists():
            raise serializers.ValidationError("Category already exists")
        return value

    class Meta:
        model = Projects
        fields = ["title", "description", "type"]


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ["title"]


class ContributorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributors
        fields = ["user_id", "project_id", "role", "permission"]


class ContributorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributors
        fields = ["user_id"]


class IssueDetailSerializer(serializers.ModelSerializer):
    def validate_title(self, value):
        if Issues.objects.filter(title=value).exists():
            raise serializers.ValidationError("Category already exists")
        return value

    class Meta:
        model = Issues
        fields = [
            "title",
            "description",
            "priority",
            "tag",
            "status",
            "created_time",
        ]


class IssueListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issues
        fields = ["title", "status"]
