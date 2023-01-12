from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Parent
from .serializer import ParentsModelSerializer




@api_view(['GET'])
def getParent(request,id):
    try:
        data= Parent.objects.get(pk=id)
        serializer= ParentsModelSerializer(data)
        return Response(serializer.data, status= status.HTTP_200_OK)
    except Parent.DoesNotExist:
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def createParent(request):
    serializer=ParentsModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updateParent(request,id):
    try:
        parent=Parent.objects.get(pk=id)
        serializer=ParentsModelSerializer(data=request.data,instance=parent)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Parent.DoesNotExist:
        return Response({},status=status.HTTP_404_NOT_FOUND)    
    


@api_view(['DELETE'])
def deletParent(request,id):
    try:
        parent=Parent.objects.get(pk=id)
        try:
            parent.delete()
            return Response({},status=status.HTTP_204_NO_CONTENT)  
        except :
            return Response({},status=status.HTTP_404_NOT_FOUND)  
    except Parent.DoesNotExist:
        return Response({},status=status.HTTP_404_NOT_FOUND)   




