from django.db import models

# Create your models here.

class Parent(models.Model):
    father_name=models.CharField(max_length=1000)
    first_mother_name=models.CharField(max_length=1000)
    last_mother_name=models.CharField(max_length=1000)

    class Meta:
        db_table='parents'


