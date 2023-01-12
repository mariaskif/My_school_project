from django.urls import path
from . import views


urlpatterns=[

path('get-user/<int:id>',views.getUsers),
path('create-user/',views.createUser),
path('update-user/<int:id>',views.updateUser),
path('delete-user/<int:id>',views.deletUser)

]