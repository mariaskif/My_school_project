from django.db import models
from subjects.models import Subject
# from class_rooms.models import Class_room
# Create your models here.
class Teacher(models.Model):
    first_name=models.CharField(max_length=1000)
    last_name=models.CharField(max_length=1000)
    salary= models.DecimalField(max_digits= 20, decimal_places= 4, default= 0)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    start_work=models.TimeField(auto_now= True)
    end_work=models.TimeField(auto_now= True)
    # classroom=models.ManyToManyField(Class_room,on_delete=models.DO_NOTHING)
    class Meta:
        db_table='teachers'             