"""my_school2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/students/', include('students.urls')),
    path('api/class-roms/', include('class_rooms.urls')),
    path('api/subjects/', include('subjects.urls')),
    path('api/teachers/', include('teachers.urls')),
    path('api/managment/', include('managment.urls')),
    path('api/manager/', include('managers.urls')),
    path('api/library/', include('libraries.urls')),
    path('api/labrotaries/', include('labrotaries.urls')),
    path('api/marks/', include('marks.urls')),
    path('api/users/',include('users.urls')),
    path('api/parents/',include('parents.urls')),


]

