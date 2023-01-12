from django.urls import path
from . import views


urlpatterns=[

path('get-managment/<int:id>/',views.getManagment),
path('create-managment/',views.createManagment),
path('update-managment/<int:id>/',views.updateManagment),
path('delete-managment/<int:id>',views.deleteManagment)

]