"""hello_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from school_management import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #test for GenericsAPIView
    #path('student/', views.StudentList.as_view(), name="student_list"),
    #path('student/<int:school_id>', views.StudentListFiltered.as_view(), name="student_specific_school_list"),
    #path('school/', views.SchoolList.as_view(), name="school_list"),

    #for ModelViewSet
    path('students/',                    views.StudentListViewSet.as_view({'get': 'list', 'post': 'create'}),                            name="student_list"),
    path('schools/',                     views.SchoolListViewSet.as_view({'get': 'list', 'post': 'create'}),                             name="school_list"),
    path('students/<int:pk>',            views.StudentListViewSet.as_view({'get': 'retrieve', 'put': 'destroy', 'delete': 'destroy'}),   name="studuent_obj"),
    path('schools/<int:pk>',             views.SchoolListViewSet.as_view({'get': 'retrieve', 'put': 'destroy', 'delete': 'destroy'}),    name="school_obj"),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
