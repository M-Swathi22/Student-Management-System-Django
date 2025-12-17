from django.contrib import admin
from .models import Student, Course, Subject, Marks, Attendance

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Marks)
admin.site.register(Attendance)