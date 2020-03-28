from django.contrib import admin
from django.utils.html import format_html

from school_management.models import School, Student

class SchoolAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="100" height="100" />'.format(obj.pic.url))
    image_tag.short_description = 'School Image'

    list_display = ("image_tag", "name", "max_student")
admin.site.register(School, SchoolAdmin)

class StudentAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="100" height="100" />'.format(obj.pic.url))
    image_tag.short_description = 'Student Image'

    def get_school(self, obj):
        return obj.school.name

    list_display = ("image_tag", "student_id", "first_name", "last_name", "get_school")
admin.site.register(Student, StudentAdmin)
