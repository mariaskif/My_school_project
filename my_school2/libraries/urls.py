from django.urls import path
from . import views


urlpatterns=[

path('get-library/<int:id>/',views.getLibrary),
path('create-library/',views.createLibrary),
path('update-library/<int:id>/',views.updateLibrary),
path('delete-library/<int:id>',views.deletLibrary)

]