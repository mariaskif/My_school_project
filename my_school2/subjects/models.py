from django.db import models
from labrotaries.models import Labrotary
# from marks.models import Mark
# Create your models here.
class Subject(models.Model):
    name=models.CharField(max_length=250)
    mark=models.DecimalField(max_digits= 20, decimal_places= 4, default= 0)
    part=models.IntegerField(default=0)
    labrotary=models.ForeignKey(Labrotary,on_delete=models.CASCADE)
    

    
    class Meta:
        db_table='subjects'
