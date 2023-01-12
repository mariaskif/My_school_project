from django.urls import path
from . import views


urlpatterns=[

path('get-manager/<int:id>/',views.getManager),
path('create-manager/',views.createManager),
path('update-manager/<int:id>/',views.updateManager),
path('delete-manager/<int:id>',views.deleteManager)

]