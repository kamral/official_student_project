from django.contrib import admin
from  .models import University,Colledge,Gymnasium,Academic
# Register your models here.
from django.forms import ModelChoiceField,ModelForm,ValidationError
from PIL import Image

# создаем форму для регулированиие размера изображения по разрешению и
# памяти которую можно закачать

# class UniversityAdmin(admin.ModelAdmin):
#     list_display = ('name','image','address','date_of_foundation',
#                     'filial','course','Faculty','direction',
#                     'Dorm_room')
#     list_display_links = ('id','name')
#     # search_fields = ('name')
#
# class ColledgeAdmin(admin.ModelAdmin):
#     list_display = ('name','image','address','date_of_foundation',
#                     'filial','course','Faculty','direction',
#                     'Dorm_room')
#     # search_fields = ('name')
#
# class GymnasiumAdmin(admin.ModelAdmin):
#     list_display = ('name', 'image', 'address', 'date_of_foundation',
#                     'filial', 'course', 'Faculty', 'direction',
#                     'Dorm_room')
#     # search_fields = ('name')
#
# class AcademicAdmin(admin.ModelAdmin):
#     list_display = ('name', 'image', 'address', 'date_of_foundation',
#                     'filial', 'course', 'Faculty', 'direction',
#                     'Dorm_room')
#     # search_fields = ('name')


admin.site.register(University)
admin.site.register(Colledge)
admin.site.register(Gymnasium)
admin.site.register(Academic)

