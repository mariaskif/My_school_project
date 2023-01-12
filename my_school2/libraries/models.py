from django.db import models

# Create your models here.
class Library(models.Model):
    number_of_sections=models.IntegerField(default=0)
    number_of_books=models.IntegerField(default=0)
    open_time=models.TimeField(auto_now= True)
    close_time=models.TimeField(auto_now= True)
    image=models.ImageField(upload_to='static/')

    class Meta:
        db_table='libraries'


