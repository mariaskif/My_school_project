from rest_framework import serializers
from .models import Subject
class SubjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model= Subject
        fields= "__all__"