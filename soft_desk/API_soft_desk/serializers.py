from pyexpat import model
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Projects, Contributors


class ProjectDetailSerializer(serializers.ModelSerializer):
    def validate_title(self, value):
        if Projects.objects.filter(title=value).exists():
            raise serializers.ValidationError("Category already exists")
        return value

    class Meta:
        model = Projects
        fields = ["title", "description", "type", "contributor"]


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ["title"]


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributors
        fields = ["user_id", "project_id", "role", "permission"]