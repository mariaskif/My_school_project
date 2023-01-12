from django.db import models
from subjects.models import Subject
# Create your models here.

class Mark (models.Model):
    marks=models.DecimalField(max_digits= 20, decimal_places= 4, default= 0)
    avarege=models.DecimalField(max_digits= 20, decimal_places= 4, default= 0)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE, related_name='sub')
    class Meta:
        db_table='marks'
