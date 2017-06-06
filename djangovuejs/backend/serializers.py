from rest_framework import serializers

from .models import Job


class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = (
            'id', 'title', 'description', 'created_at', 'updated_at'
        )