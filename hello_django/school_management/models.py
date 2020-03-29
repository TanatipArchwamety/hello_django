import uuid
from django.core.exceptions import ValidationError
from django.conf import settings
from django.db import models
from django import forms

class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()

class School(models.Model):
    id              = models.AutoField(primary_key=True)
    pic             = models.ImageField(upload_to="school/", height_field=None, width_field=None, max_length=100, default = 'school/no-img.jpg')
    name            = models.CharField(max_length=20)
    max_student     = models.PositiveIntegerField()

    def __str__(self):
        return self.name + "(max: %d)"%self.max_student

    #check when modify max_student capacity
    def save(self, *args, **kwargs):
        check_school_capacity = self.max_student
        if self.student_set.count() > check_school_capacity:
            raise ValidationError(settings.SCHOOL_FULL_ERR_MSG)
        super(School, self).save(*args, **kwargs)

class Student(models.Model):
    id              = models.AutoField(primary_key=True)
    pic             = models.ImageField(upload_to="student/", height_field=None, width_field=None, max_length=100, default = 'student/no-img.jpg')
    student_id      = models.CharField(max_length=20)
    first_name      = models.CharField(max_length=20)
    last_name       = models.CharField(max_length=20)
    nationality     = models.CharField(max_length=50)
    school          = models.ForeignKey(School, on_delete=models.PROTECT )
    unique_identification_string    = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return "%s %s" % (self.first_name , self.last_name)

    #check when add student exceeding school's max_student capacity
    def create(self, *args, **kwargs):
        self.unique_identification_string = uuid.uuid4().hex
        check_school_capacity = self.school.max_student
        if self.school.student_set.count() >= check_school_capacity:
            raise ValidationError(settings.SCHOOL_FULL_ERR_MSG)
        super(Student, self).create(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.unique_identification_string = uuid.uuid4().hex
        check_school_capacity = self.school.max_student
        if self.school.student_set.count() >= check_school_capacity:
            raise ValidationError(settings.SCHOOL_FULL_ERR_MSG)
        super(Student, self).save(*args, **kwargs)
