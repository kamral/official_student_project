from django.contrib import admin
from  .models import University,Colledge,Gymnasium
# Register your models here.
from django.forms import ModelChoiceField,ModelForm,ValidationError
from PIL import Image






admin.site.register(University)
admin.site.register(Colledge)
admin.site.register(Gymnasium)

