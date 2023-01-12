from rest_framework import serializers
from .models import Mark


class ArchModelSerializer(serializers.ModelSerializer):
    class Meta:
        model= Mark
        fields= "__all__"

