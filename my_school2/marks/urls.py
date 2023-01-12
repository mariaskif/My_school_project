from django.urls import path
from . import views


urlpatterns=[

path('getavg/marks/',views.getAvg),
path('get-archieve/<int:id>/',views.getArch),
path('create-archieve/',views.createArch),
path('update-archieve/<int:id>/',views.updateArch),
path('delete-archieve/<int:id>',views.deletArch)

]