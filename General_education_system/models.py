from django.db import models
from student.models import Faculty,Course,Direction
# Create your models here.
from PIL import Image
from student.models import *








class University(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date_of_foundation = models.DateTimeField(auto_now_add=True, )
    filial_of_university = models.CharField(max_length=100, verbose_name='Филиал университета', blank=True)
    # course=models.ForeignKey()

class Colledge(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date_of_foundation = models.DateTimeField(auto_now_add=True, )
    filial_of_university = models.CharField(max_length=100, verbose_name='Филиал университета', blank=True)


class Academic(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date_of_foundation = models.DateTimeField(auto_now_add=True, )
    filial_of_university = models.CharField(max_length=100, verbose_name='Филиал университета', blank=True)


class Gymnasium(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date_of_foundation = models.DateTimeField(auto_now_add=True, )
    filial_of_university = models.CharField(max_length=100, verbose_name='Филиал университета', blank=True)
