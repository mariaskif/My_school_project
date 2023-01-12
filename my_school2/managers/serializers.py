from rest_framework import serializers
from .models import Manager
class ManagernttModelSerializer(serializers.ModelSerializer):
    class Meta:
        model= Manager
        fields= "__all__"