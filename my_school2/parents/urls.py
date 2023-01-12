from django.urls import path
from . import views


urlpatterns=[

path('get-parent/<int:id>/',views.getParent),
path('create-parent/',views.createParent),
path('update-parent/<int:id>/',views.updateParent),
path('delete-parent/<int:id>',views.deletParent)

]