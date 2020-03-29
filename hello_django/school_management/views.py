from django.shortcuts import render
from rest_framework import status, generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


from school_management.models import Student, School
from school_management.serializers import StudentSerializer, SchoolSerializer
# Create your views here.

#function based view
"""
@api_view(['POST'])
def student_list(request):
    students = Student.objects.all()
    response_data = list()
    response_data.append({  'method': request.method,
                            'data': request.data
                        })
    for student in students:
        student_data = dict()
        student_data['pic'] = student.pic.url
        student_data['student_id'] = student.student_id
        student_data['first_name'] = student.first_name
        student_data['last_name'] = student.last_name
        student_data['school'] = student.school.name
        response_data.append(student_data)

    return Response(status=status.HTTP_200_OK, data=response_data)

#full class based view
class StudentList(APIView):
    def __create_student_list(self):
        student_list = list()
        for student in Student.objects.all():
            student_data = dict()
            student_data['pic'] = student.pic.url
            student_data['student_id'] = student.student_id
            student_data['first_name'] = student.first_name
            student_data['last_name'] = student.last_name
            student_data['school'] = student.school.name
            student_list.append(student_data)
        return student_list

    def __create_response_list(self, request):
        response_data = list()
        response_data.append({  'method': request.method,
                                'data': request.data
                            })
        return response_data

    def post(self, request):
        response_data = self.__create_response_list(request)
        response_data.append(self.__create_student_list())
        return Response(status=status.HTTP_200_OK, data=response_data)

    def get(self, request):
        response_data = self.__create_response_list(request)
        response_data.append(self.__create_student_list())
        return Response(status=status.HTTP_200_OK, data=response_data)
"""

#short class based view with serializer, GenericsAPIView
class StudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentListFiltered(generics.ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        school_id = self.kwargs["school_id"]
        return Student.objects.filter(school__id=school_id)

class SchoolList(generics.ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


