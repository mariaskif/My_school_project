from django.db import models
from teachers.models import Teacher
# Create your models here.
class Class_room(models.Model):
    name=models.CharField(max_length=250)
    number_of_students=models.IntegerField(default=0)
    teachers= models.ManyToManyField(Teacher)

    class Meta:
        db_table='class_rooms'
