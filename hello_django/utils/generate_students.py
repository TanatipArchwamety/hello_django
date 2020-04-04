#!/usr/bin/env python

import os
import sys
import django
from faker import Faker

def generate_students(times):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello_django.settings')
    django.setup()
    from school_management.models import Student,School

    nationality_pool = ['Australian', 'English', 'French', 'American']
    school_pool = [s for s in School.objects.all()]
    fake = Faker()

    for i in range(times):
        name = fake.name().split()
        student_id = str(fake.random.randint(10000000,99999999))
        school = school_pool[fake.random.randint(0,len(school_pool)-1)]
        nationality = nationality_pool[fake.random.randint(0,len(nationality_pool)-1)]

        Student.objects.create( student_id  = student_id,
                                first_name  = name[0],
                                last_name   = name[1],
                                school      = school,
                                nationality = nationality
                              )


if __name__ == '__main__':
    generate_students(200)
