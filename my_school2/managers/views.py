from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Manager
from .serializers import ManagernttModelSerializer




@api_view(['GET'])
def getManager(request,id):
    try:
        data= Manager.objects.get(pk=id)
        serializer= ManagernttModelSerializer(data)
        return Response(serializer.data, status= status.HTTP_200_OK)
    except Manager.DoesNotExist:
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def createManager(request):
    serializer=ManagernttModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updateManager(request,id):
    try:
        manager=Manager.objects.get(pk=id)
        serializer=ManagernttModelSerializer(data=request.data,instance=manager)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Manager.DoesNotExist:
        return Response({},status=status.HTTP_404_NOT_FOUND)    
    


@api_view(['DELETE'])
def deleteManager(request,id):
    try:
        man=Manager.objects.get(pk=id)
        try:
            man.delete()
            return Response({},status=status.HTTP_204_NO_CONTENT)  
        except :
            return Response({},status=status.HTTP_404_NOT_FOUND)  
    except Manager.DoesNotExist:
        return Response({},status=status.HTTP_404_NOT_FOUND)   



