from django.contrib import admin
from django.forms import ModelForm,ValidationError
# Register your models here.
from  PIL import Image

from .models import *





admin.site.register(Student)
admin.site.register(Room)
admin.site.register(Direction)
admin.site.register(Course)
admin.site.register(Faculty)
admin.site.register(Dorm_room)

