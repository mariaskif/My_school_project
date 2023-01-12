from django.urls import path
from . import views


urlpatterns=[

path('get-labrotary/<int:id>/',views.getLabrotary),
path('create-labrotary/',views.createLabrotary),
path('update-labrotary/<int:id>/',views.updateLabrotary),
path('delete-labrotary/<int:id>',views.deletLabrtary)

]