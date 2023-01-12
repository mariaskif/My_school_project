from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from  class_rooms.models import Class_room
from .serializers import (
StudentModelSerializer,
StudentSerializer,
Studentparent,
StudentclassSerializer,
Searchclass,
Searchparentsclass
)
from django.db.models import Avg, Count, Min, Sum





# Author.objects.annotate(total_pages=Sum('book__pages'))
@api_view(['GET'])
def getcount(request):
  countOf=Student.objects.count()
  return Response(countOf,status=status.HTTP_200_OK)



@api_view(['GET'])
def getparentsclass(request):
    serializer=Searchclass(data=request.data)
    if serializer.is_valid():
        serializersearch=serializer.data
        classrom=Class_room.objects.filter(name=serializersearch['name'])
        classromms=Searchparentsclass(classrom,many=True)
        return Response(classromms.data, status=status.HTTP_200_OK)
    return Response(classromms.errors,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def getstudentclass(request):
    serializer=Searchclass(data=request.data)
    if serializer.is_valid():
        serializersearch=serializer.data
        classrom=Class_room.objects.filter(name=serializersearch['name'])
        classromms=StudentclassSerializer(classrom,many=True)
        return Response(classromms.data , status=status.HTTP_200_OK)
    return Response(classromms.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getStudentmark(request,id):
    data= Student.objects.get(pk=id)
    serializer=StudentSerializer(data)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def getStudentparents(request,id):
    data= Student.objects.get(pk=id)
    serializer=Studentparent(data)
    return Response(serializer.data,status=status.HTTP_200_OK)

   
@api_view(['GET'])
def getStudent(request,id):
    try:
        data= Student.objects.get(pk=id)
        serializer= StudentModelSerializer(data)
        return Response(serializer.data, status= status.HTTP_200_OK)
    except Student.DoesNotExist:
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def createStudent(request):
    serializer=StudentModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updateStudent(request,id):
    try:
        student=Student.objects.get(pk=id)
        serializer=StudentModelSerializer(data=request.data,instance=student)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Student.DoesNotExist:
        return Response({},status=status.HTTP_404_NOT_FOUND)    
    


@api_view(['DELETE'])
def deletStudent(request,id):
    try:
        student=Student.objects.get(pk=id)
        try:
            student.delete()
            return Response({},status=status.HTTP_204_NO_CONTENT)  
        except :
            return Response({},status=status.HTTP_404_NOT_FOUND)  
    except Student.DoesNotExist:
        return Response({},status=status.HTTP_404_NOT_FOUND)   

