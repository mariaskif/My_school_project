from django.urls import path
from . import views


urlpatterns=[
 path('student/<int:id>/marks/',views.getStudentmark),
  path('student/<int:id>/parents/',views.getStudentparents),
  path('class/students/',views.getstudentclass),
  path('class/students/parents/',views.getparentsclass),

  path('count/students/',views.getcount),



path('get-student/<int:id>/',views.getStudent),
path('create-student/',views.createStudent),
path('update-student/<int:id>/',views.updateStudent),
path('delete-student/<int:id>',views.deletStudent)

]