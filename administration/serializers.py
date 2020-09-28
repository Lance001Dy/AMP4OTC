from rest_framework import serializers
from .models import ProjectAdministration

class ProjectAdministrationSerializer(serializers.Serializer):
    ProjectAdministration.project_specifications.site_name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    ProjectAdministration.project_specifications.section_name = serializers.CharField(required=False, allow_blank=True, max_length=100)

    def create(self, validated_data):
        """
        Create and return a new `Administration` instance, given the validated data.
        """
        return ProjectAdministration.objects.create(**validated_data)