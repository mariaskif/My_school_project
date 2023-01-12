from django.db import models

# Create your models here.
class Labrotary(models.Model):
    name=models.CharField(max_length=250)
    open_time=models.TimeField(auto_now= True)
    close_time=models.TimeField(auto_now= True)

        
    class Meta:
        db_table='labroteries'