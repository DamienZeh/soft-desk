from rest_framework import serializers
from .models import Comments, Projects, Contributors, Issues


class ProjectDetailSerializer(serializers.ModelSerializer):
    author_user_name = serializers.CharField(
        source="author_user_id.username", read_only=True
    )

    def validate_title(self, value):
        if Projects.objects.filter(title=value).exists():
            raise serializers.ValidationError("Category already exists")
        return value

    class Meta:
        model = Projects
        fields = [
            "title",
            "description",
            "type",
            "author_user_name",
            "author_user_id",
        ]


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ["title"]


class ContributorDetailSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(
        source="user_id.username", read_only=True
    )
    project_name = serializers.CharField(
        source="project_id.title", read_only=True
    )

    class Meta:
        model = Contributors
        fields = [
            "user_name",
            "user_id",
            "project_name",
            "project_id",
            "role",
            "permission",
        ]


class ContributorListSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(
        source="user_id.username", read_only=True
    )

    class Meta:
        model = Contributors
        fields = ["user_name", "user_id"]


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
            "author_user_id",
        ]


class IssueListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issues
        fields = ["title", "status"]


class CommentDetailSerializer(serializers.ModelSerializer):
    issue_name_response = serializers.CharField(
        source="issue_id.title", read_only=True
    )

    def validate_description(self, value):
        if Comments.objects.filter(description=value).exists():
            raise serializers.ValidationError("Category already exists")
        return value

    class Meta:
        model = Comments
        fields = [
            "description",
            "created_time",
            "author_user_id",
            "issue_name_response",
            "issue_id",
        ]


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = [
            "description",
        ]
