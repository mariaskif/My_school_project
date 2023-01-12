from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Class_room
from teachers.models import Teacher
from .serializers import Subjectserializer, classroomModelSerializer,TeacherSerializer


# @api_view(['GET'])
# def 



@api_view(['GET'])
def getSubject(request,id):
    data= Class_room.objects.get(pk=id)
    # data= Class_room.objects.filter(teachers=teacher_id)
    serializer=Subjectserializer(data)
    return Response(serializer.data,status=status.HTTP_200_OK)



@api_view(['GET'])
def getTeachers(request,id):
    data= Class_room.objects.get(pk=id)
    serializer=TeacherSerializer(data)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['GET'])
def getClass(request,id):
    try:
        data= Class_room.objects.get(pk=id)
        serializer= classroomModelSerializer(data)
        return Response(serializer.data, status= status.HTTP_200_OK)
    except Class_room.DoesNotExist:
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def createClass(request):
    serializer=classroomModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updateClass(request,id):
    try:
        classroom=Class_room.objects.get(pk=id)
        serializer=classroomModelSerializer(data=request.data,instance=classroom)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Class_room.DoesNotExist:
        return Response({},status=status.HTTP_404_NOT_FOUND)    
    


@api_view(['DELETE'])
def deletClass(request,id):
    try:
        classroom=Class_room.objects.get(pk=id)
        try:
            classroom.delete()
            return Response({},status=status.HTTP_204_NO_CONTENT)  
        except :
            return Response({},status=status.HTTP_404_NOT_FOUND)  
    except Class_room.DoesNotExist:
        return Response({},status=status.HTTP_404_NOT_FOUND)   


