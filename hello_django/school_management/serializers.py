from school_management.models import Student, School
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ("pic", "student_id", "first_name", "last_name", "school")

class SchoolSerializer(serializers.ModelSerializer):
    curr_student = serializers.SerializerMethodField()

    def get_curr_student(self, obj):
        return obj.student_set.count()

    class Meta:
        model = School
        fields = ("pic", "name", "max_student", "curr_student")
