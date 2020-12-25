from django.contrib import admin
from  .models import University,Colledge,Gymnasium,Academic
# Register your models here.
from django.forms import ModelChoiceField,ModelForm,ValidationError
from PIL import Image

# создаем форму для регулированиие размера изображения по разрешению и
# памяти которую можно закачать


admin.site.register(University)
admin.site.register(Colledge)
admin.site.register(Gymnasium)
admin.site.register(Academic)

