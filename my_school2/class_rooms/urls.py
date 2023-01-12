from django.urls import path
from . import views


urlpatterns=[
path('class/<int:id>/teachers/',views.getTeachers),
path('class/<int:id>/subject/',views.getSubject),

path('get-classRoom/<int:id>/',views.getClass),
path('create-classRoom/',views.createClass),
path('update-classRoom/<int:id>/',views.updateClass),
path('delete-classRoom/<int:id>',views.deletClass)


]