from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Teacher
from .serializers import TeacherModelSerializer




@api_view(['GET'])
def getTeachers(request,id):
    try:
        data= Teacher.objects.get(pk=id)
        serializer= TeacherModelSerializer(data)
        return Response(serializer.data, status= status.HTTP_200_OK)
    except Teacher.DoesNotExist:
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def createTeacher(request):
    serializer=TeacherModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updateTeacher(request,id):
    try:
        teacher=Teacher.objects.get(pk=id)
        serializer=TeacherModelSerializer(data=request.data,instance=teacher)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Teacher.DoesNotExist:
        return Response({},status=status.HTTP_404_NOT_FOUND)    
    


@api_view(['DELETE'])
def deletTeacher(request,id):
    try:
        teacher=Teacher.objects.get(pk=id)
        try:
            teacher.delete()
            return Response({},status=status.HTTP_204_NO_CONTENT)  
        except :
            return Response({},status=status.HTTP_404_NOT_FOUND)  
    except Teacher.DoesNotExist:
        return Response({},status=status.HTTP_404_NOT_FOUND)            
