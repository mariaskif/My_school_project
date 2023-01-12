from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Mark
from .serializers import ArchModelSerializer
from django.db.models import Avg

from django.db.models import Avg, Count, Min, Sum



@api_view(['GET'])
def getAvg(request):
    
        avg=Mark.objects.aggregate(Avg('marks'))
        return Response(avg , status= status.HTTP_200_OK)



# Member.objects.aggregate(Avg('wins'))
# Member.objects.aggregate(Avg('losses'))

@api_view(['GET'])
def getArch(request,id):
    try:
        data= Mark.objects.get(pk=id)
        serializer= ArchModelSerializer(data)
        return Response(serializer.data, status= status.HTTP_200_OK)
    except Mark.DoesNotExist:
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def createArch(request):
    serializer=ArchModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updateArch(request,id):
    try:
        archieve=Mark.objects.get(pk=id)
        serializer=ArchModelSerializer(data=request.data,instance=archieve)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Mark.DoesNotExist:
        return Response({},status=status.HTTP_404_NOT_FOUND)    
    


@api_view(['DELETE'])
def deletArch(request,id):
    try:
        arch=Mark.objects.get(pk=id)
        try:
            arch.delete()
            return Response({},status=status.HTTP_204_NO_CONTENT)  
        except :
            return Response({},status=status.HTTP_404_NOT_FOUND)  
    except Mark.DoesNotExist:
        return Response({},status=status.HTTP_404_NOT_FOUND)   



