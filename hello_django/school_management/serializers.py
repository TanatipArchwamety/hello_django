import uuid
from school_management.models import Student, School
from rest_framework import serializers
from django.conf import settings

class SchoolSerializer(serializers.ModelSerializer):
    curr_student = serializers.SerializerMethodField()

    def get_curr_student(self, obj):
        return obj.student_set.count()

    class Meta:
        model = School
        fields = ("id", "pic", "name", "max_student", "curr_student")

class StudentSerializer(serializers.ModelSerializer):
    #school = SchoolSerializer()

    def validate(self, data):
        school_obj = data["school"]
        if school_obj.student_set.count() >= school_obj.max_student:
            raise serializers.ValidationError({"error":settings.SCHOOL_FULL_ERR_MSG})
        return data

    def create(self, validated_data):
        student = Student.objects.create(**validated_data)
        student.unique_identification_string = uuid.uuid4().hex
        student.save()
        return student

    class Meta:
        model = Student
        fields = ("id", "pic", "student_id", "first_name", "last_name", "nationality", "school")
