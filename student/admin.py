from django.contrib import admin
from django.forms import ModelForm,ValidationError
# Register your models here.
from  PIL import Image

from .models import Student,\
    Room,\
    Direction,\
    Course,\
    Faculty,Dorm_room

class BaseAdminForm(ModelForm):
   # минимальное разрешение для фотов комнате
    min_resolution=(400,400)
   # максимлаьное разрешение для фото в комнате
    max_resolution=(2400,1200)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['student_photo'].help_text='Загружайте изображение с мин разрешением {} x {}'.format(*self.min_resolution)

    def clean_image(self):
        image=self.cleaned_data['student_photo']
        img=Image.open(image)
        # print(img.heigt,img.width)
        min_height, min_width=self.min_resolution
        if img.height <min_height or img.width < min_width:
            raise ValidationError('Загруженное изображение меньше положенного')
        return image


class RoomAdmin(admin.ModelAdmin):
    form=BaseAdminForm


admin.site.register(Student)
admin.site.register(Room,RoomAdmin)
admin.site.register(Direction)
admin.site.register(Course)
admin.site.register(Faculty)
admin.site.register(Dorm_room)

