from django.urls import path
from . import views


urlpatterns=[

path('get-teacher/<int:id>',views.getTeachers,name='getTeachers'),
path('create-teacher/',views.createTeacher,name='createTeacher'),
path('update-teacher/<int:id>',views.updateTeacher,name='updateTeacher'),
path('delete-teacher/<int:id>',views.deletTeacher,name='deleteTeacher')

]






