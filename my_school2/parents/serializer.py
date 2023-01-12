from rest_framework import serializers
from .models import Parent


class ParentsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model= Parent
        fields= "__all__"