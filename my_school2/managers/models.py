from django.db import models
# from managment.models import Managment
# Create your models here.

class Manager(models.Model):
    name=models.CharField(max_length=250)
    statrt_work=models.TimeField(auto_now=True)
    end_work=models.TimeField(auto_now=True)
    # section=models.OneToOneField(Managment,on_delete=models.DO_NOTHING)

    class Meta:
        db_table='managers'

