from rest_framework import serializers
from .models import Labrotary


class LabrotaryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model= Labrotary
        fields= "__all__"