from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User

class Usersrializer(serializers.Serializer):
    id= serializers.IntegerField(read_only= True)
    username=serializers.CharField(max_length=250)
    password=serializers.CharField(max_length=250)
    email=serializers.EmailField(max_length=1000)
    
    def update(self,instance,validated_data):
        instance.username=validated_data.get('username' ,instance.username)
        instance.email=validated_data.get('email' ,instance.email)
        instance.password=validated_data.get('password',instance.password)
        instance.save()
        return instance