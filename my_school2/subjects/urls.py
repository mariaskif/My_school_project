from django.urls import path
from . import views


urlpatterns=[

path('get-subject/<int:id>/',views.getSubject,name='getSubject'),
path('create-subject/',views.createSubject,name='createSubject'),
path('update-subject/<int:id>/',views.updateSubject,name='updateSubject'),
path('delete-subject/<int:id>',views.deletSubject,name='deletSubject')

]