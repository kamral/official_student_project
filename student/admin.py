from django.contrib import admin
from django.forms import ModelForm,ValidationError
# Register your models here.
from  PIL import Image

from .models import Student,\
    Room,\
    Direction,\
    Course,\
    Faculty,Dorm_room

class NotebookAdminForm(ModelForm):
    min_resolution=(400,400)
    max_resolution=(2400,1200)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['image'].help_text='Загружайте изображение с мин разрешением {} x {}'.format(*self.min_resolution)

    def clean_image(self):
        image=self.cleaned_data['image']
        img=Image.open(image)
        # print(img.heigt,img.width)
        min_height, min_width=self.min_resolution
        if img.height <min_height or img.width < min_width:
            raise ValidationError('Загруженное изображение меньше положенного')
        return image


admin.site.register(Student)
admin.site.register(Room)
admin.site.register(Direction)
admin.site.register(Course)
admin.site.register(Faculty)
admin.site.register(Dorm_room)

