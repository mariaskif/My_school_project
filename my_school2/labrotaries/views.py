from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Labrotary
from .serializers import LabrotaryModelSerializer




@api_view(['GET'])
def getLabrotary(request,id):
    try:
        data= Labrotary.objects.get(pk=id)
        serializer= LabrotaryModelSerializer(data)
        return Response(serializer.data, status= status.HTTP_200_OK)
    except Labrotary.DoesNotExist:
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def createLabrotary(request):
    serializer=LabrotaryModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updateLabrotary(request,id):
    try:
        labrotary=Labrotary.objects.get(pk=id)
        serializer=LabrotaryModelSerializer(data=request.data,instance=labrotary)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Labrotary.DoesNotExist:
        return Response({},status=status.HTTP_404_NOT_FOUND)    
    


@api_view(['DELETE'])
def deletLabrtary(request,id):
    try:
        lab=Labrotary.objects.get(pk=id)
        try:
            lab.delete()
            return Response({},status=status.HTTP_204_NO_CONTENT)  
        except :
            return Response({},status=status.HTTP_404_NOT_FOUND)  
    except Labrotary.DoesNotExist:
        return Response({},status=status.HTTP_404_NOT_FOUND)   



