from django.contrib import admin

# Register your models here.

from .models import student,\
    Room,\
    Direction,\
    Course,\
    Faculty

admin.site.register(student)
admin.site.register(Room)
admin.site.register(Direction)
admin.site.register(Course)
admin.site.register(Faculty)
