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


class Student(models.Model):
    id              = models.AutoField(primary_key=True)
    pic             = models.ImageField(upload_to="student/", height_field=None, width_field=None, max_length=100, default = 'student/no-img.jpg')
    student_id      = models.CharField(max_length=20)
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    school          = models.ForeignKey(School, on_delete=models.PROTECT )

    def __str__(self):
        return "%s %s" % (self.first_name , self.last_name)
