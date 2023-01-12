from rest_framework import serializers
from .models import Student
from  marks.models import Mark
from  parents.models import Parent
from  marks.serializers import ArchModelSerializer
from  parents.serializer import ParentsModelSerializer
# from  class_rooms.serializers import classroomModelSerializer
class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model= Student
        fields= "__all__"


class StudentparentsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model= Student
        fields=['parent']
       

       
class StudentSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    marks=ArchModelSerializer()

class Studentparent(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    first_name=serializers.CharField(max_length=250)
    last_name=serializers.CharField(max_length=250)
    parent=ParentsModelSerializer()


class StudentclassSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    students=StudentModelSerializer(many=True)
    name=serializers.CharField(max_length=250)


class Searchclass(serializers.Serializer):
   name=serializers.CharField(max_length=250)


class Searchparentsclass(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    students=StudentparentsModelSerializer(many=True)
    name=serializers.CharField(max_length=250)