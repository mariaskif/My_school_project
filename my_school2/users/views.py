from django.shortcuts import render
from django.contrib.auth.models  import User 
from  rest_framework.decorators import api_view
from rest_framework import status 
from rest_framework.response import Response

from .serializers import Usersrializer
    

@api_view(['GET'])
def getUsers(request,id):
    try:
        user= User.objects.get(pk=id)
        serializer=Usersrializer(user)
        return Response(serializer.data, status= status.HTTP_200_OK)
    except User.DoesNotExist:
         return Response({},status=status.HTTP_404_NOT_FOUND)


api_view(['POST'])
def createUser (request):
    serializer=Usersrializer(data=request.data)
    if serializer.is_valid():
        userdata=serializer.data
        User.objects.create_user(username=userdata['username'],password=userdata['password'],email=userdata['email'])
        return Response({},status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updateUser(request,id):
    try:
        user=User.objects.get(pk=id)
        serializer=Usersrializer(data=request.data,instance=user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return Response({},status=status.HTTP_404_NOT_FOUND)    
    
  


@api_view(['DELETE'])
def deletUser(request,id):
    try:
        user=User.objects.get(pk=id)
        try:
            user.delete()
            return Response({},status=status.HTTP_204_NO_CONTENT)  
        except :
            return Response({},status=status.HTTP_404_NOT_FOUND)  
    except User.DoesNotExist:
        return Response({},status=status.HTTP_404_NOT_FOUND) 

