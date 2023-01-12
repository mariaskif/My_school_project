from django.db import models
from class_rooms.models import Class_room
from marks.models import Mark
from parents.models import Parent
# Create your models here.

class Student(models.Model):
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=250)
    class_room=models.ForeignKey(Class_room,on_delete=models.CASCADE,related_name='students',related_query_name='student')
    marks=models.ForeignKey(Mark,on_delete=models.CASCADE)
    parent=models.ForeignKey(Parent,on_delete=models.CASCADE)
    class Meta:
        db_table='students'
