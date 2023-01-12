from rest_framework import serializers
from .models import Class_room
from teachers.models import Teacher
from teachers.serializers import TeacherModelSerializer,teacherModelSubject
# from subjects.serializers import SubjectModelSerializer
class classroomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model= Class_room
        fields= "__all__"




class TeacherSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    teachers=TeacherModelSerializer(many=True)

class Subjectserializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    teachers=teacherModelSubject(many=True)
    # teachers=serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all(),many=True)
    #  teachers_sub=serializers.CharField(max_length=250,source='teachers.first_name')



