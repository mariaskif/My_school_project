from rest_framework import serializers
from .models import Library


class LibraryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model= Library
        fields= "__all__"