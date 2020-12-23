from django.contrib import admin

# Register your models here.

from .models import Student,\
    Room,\
    Direction,\
    Course,\
    Faculty,Dorm_room

admin.site.register(Student)
admin.site.register(Room)
admin.site.register(Direction)
admin.site.register(Course)
admin.site.register(Faculty)
admin.site.register(Dorm_room)

