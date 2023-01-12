from rest_framework import serializers
from .models import Managment
class ManahmenttModelSerializer(serializers.ModelSerializer):
    class Meta:
        model= Managment
        fields= "__all__"