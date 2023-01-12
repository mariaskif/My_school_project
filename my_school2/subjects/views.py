from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Subject
from .serializers import SubjectModelSerializer




@api_view(['GET'])
def getSubject(request,id):
    try:
        data= Subject.objects.get(pk=id)
        serializer= SubjectModelSerializer(data)
        return Response(serializer.data, status= status.HTTP_200_OK)
    except Subject.DoesNotExist:
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def createSubject(request):
    serializer=SubjectModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updateSubject(request,id):
    try:
        subject=Subject.objects.get(pk=id)
        serializer=SubjectModelSerializer(data=request.data,instance=subject)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except subject.DoesNotExist:
        return Response({},status=status.HTTP_404_NOT_FOUND)    
    


@api_view(['DELETE'])
def deletSubject(request,id):
    try:
        subject=Subject.objects.get(pk=id)
        try:
            subject.delete()
            return Response({},status=status.HTTP_204_NO_CONTENT)  
        except :
            return Response({},status=status.HTTP_404_NOT_FOUND)  
    except Subject.DoesNotExist:
        return Response({},status=status.HTTP_404_NOT_FOUND)   