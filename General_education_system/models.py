from django.db import models

# Create your models here.



class University(models.Model):
    name_university=models.CharField(max_length=100,verbose_name='Название университета')
    address_university=models.CharField(max_length=100,verbose_name='Адрес университета')
