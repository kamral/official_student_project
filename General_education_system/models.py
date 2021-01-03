from django.db import models
# Create your models here.
from PIL import Image
from django.urls import reverse

from student.models import *


#
# class Education_(models.Model):
#     image = models.ImageField()
#     name = models.CharField(max_length=100)
#     address = models.CharField(max_length=100)
#     date_of_foundation = models.DateTimeField(auto_now_add=True, )
#     filial = models.CharField(max_length=100, verbose_name='Филиал университета', blank=True)
#     # course=models.ForeignKey(Course,on_delete=models.CASCADE)
#     # Faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE)
#     # direction=models.ForeignKey(Direction,on_delete=models.CASCADE)
#     # Dorm_room=models.ForeignKey(Dorm_room,on_delete=models.CASCADE)
#
#
#
#
# class University(BaseModel):
#     pass
#
# class Colledge(models.Model):
#     pass
#
# class Academic(models.Model):
#     pass
#
# class Gymnasium(models.Model):
#     pass


class General_education_system(models.Model):
    image = models.ImageField(upload_to='photo/')
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date_of_foundation = models.DateTimeField(auto_now_add=True, )
    filial = models.CharField(max_length=100, verbose_name='Филиал университета', blank=True)
    category=models.ForeignKey('Category_education',on_delete=models.CASCADE)
    history_of_university=models.TextField()


    def __str__(self):
        return self.name

class Category_education(models.Model):
    name=models.CharField(max_length=100,verbose_name='Общеобразовательная система')

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id'})

    def __str__(self):
        return self.name