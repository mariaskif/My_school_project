from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Library
from .serializers import LibraryModelSerializer




@api_view(['GET'])
def getLibrary(request,id):
    try:
        data= Library.objects.get(pk=id)
        serializer= LibraryModelSerializer(data)
        return Response(serializer.data, status= status.HTTP_200_OK)
    except Library.DoesNotExist:
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def createLibrary(request):
    serializer=LibraryModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updateLibrary(request,id):
    try:
        library=Library.objects.get(pk=id)
        serializer=LibraryModelSerializer(data=request.data,instance=library)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Library.DoesNotExist:
        return Response({},status=status.HTTP_404_NOT_FOUND)    
    


@api_view(['DELETE'])
def deletLibrary(request,id):
    try:
        lib=Library.objects.get(pk=id)
        try:
            lib.delete()
            return Response({},status=status.HTTP_204_NO_CONTENT)  
        except :
            return Response({},status=status.HTTP_404_NOT_FOUND)  
    except Library.DoesNotExist:
        return Response({},status=status.HTTP_404_NOT_FOUND)   


