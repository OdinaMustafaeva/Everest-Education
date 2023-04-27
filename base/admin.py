from django.contrib import admin
from .models import location, course, subjects, teacher, students,  ielts, Profile

admin.site.register(location)
admin.site.register(course)
admin.site.register(subjects)
admin.site.register(teacher)
admin.site.register(students)

admin.site.register(ielts)
admin.site.register(Profile)
