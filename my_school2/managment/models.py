from django.db import models
from managers.models import Manager
# Create your models here.
class Managment(models.Model):
    name=models.CharField(max_length=250)
    manager=models.OneToOneField(Manager,on_delete=models.CASCADE,related_name='my_manager')

    class Meta:
        db_table='section'
