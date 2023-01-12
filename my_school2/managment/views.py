from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Managment
from .serializers import ManahmenttModelSerializer




@api_view(['GET'])
def getManagment(request,id):
    try:
        data= Managment.objects.get(pk=id)
        serializer= ManahmenttModelSerializer(data)
        return Response(serializer.data, status= status.HTTP_200_OK)
    except Managment.DoesNotExist:
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def createManagment(request):
    serializer=ManahmenttModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updateManagment(request,id):
    try:
        managment=Managment.objects.get(pk=id)
        serializer=ManahmenttModelSerializer(data=request.data,instance=managment)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Managment.DoesNotExist:
        return Response({},status=status.HTTP_404_NOT_FOUND)    
    


@api_view(['DELETE'])
def deleteManagment(request,id):
    try:
        man=Managment.objects.get(pk=id)
        try:
            man.delete()
            return Response({},status=status.HTTP_204_NO_CONTENT)  
        except :
            return Response({},status=status.HTTP_404_NOT_FOUND)  
    except Managment.DoesNotExist:
        return Response({},status=status.HTTP_404_NOT_FOUND)   


