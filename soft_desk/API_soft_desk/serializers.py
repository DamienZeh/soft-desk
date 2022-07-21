from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Projects


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Projects
        fields = ["title", "description", "type"]
