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
from rest_framework_nested.routers import SimpleRouter, NestedSimpleRouter
#from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from school_management.views import StudentListViewSet, SchoolListViewSet

#NESTED
router = SimpleRouter()
router.register(r'schools', SchoolListViewSet)
schools_router = NestedSimpleRouter(router, r'schools', lookup='school')
schools_router.register(r'students', StudentListViewSet)

#SIMPLE
#router = DefaultRouter()
#router.register(r'schools', SchoolListViewSet)
#router.register(r'students', StudentListViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),

    #for drf-nested-routers
    path('', include(router.urls)),
    path('', include(schools_router.urls)),

    #for default routers
    #path('', include(router.urls)),

    #test for GenericsAPIView
    #path('student/', StudentList.as_view(), name="student_list"),
    #path('student/<int:school_id>', StudentListFiltered.as_view(), name="student_specific_school_list"),
    #path('school/', SchoolList.as_view(), name="school_list"),

    #for ModelViewSet
    #path('students/',                    StudentListViewSet.as_view({'get': 'list', 'post': 'create'}),                            name="student_list"),
    #path('schools/',                     SchoolListViewSet.as_view({'get': 'list', 'post': 'create'}),                             name="school_list"),
    #path('students/<int:pk>',            StudentListViewSet.as_view({'get': 'retrieve', 'put': 'destroy', 'delete': 'destroy'}),   name="studuent_obj"),
    #path('schools/<int:pk>',             SchoolListViewSet.as_view({'get': 'retrieve', 'put': 'destroy', 'delete': 'destroy'}),    name="school_obj"),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
