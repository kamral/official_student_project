from django.db import models

# Create your models here.



class University(models.Model):
    image_university=models.ImageField(verbose_name='Фото университета')
    name_university=models.CharField(max_length=100,verbose_name='Название университета')
    address_university=models.CharField(max_length=100,verbose_name='Адрес университета')
    date_of_foundation=models.DateTimeField(auto_now_add=True,verbose_name='Дата основания')
    filial_of_university=models.CharField(max_length=100, verbose_name='Филиал университета', blank=True)


class Colledge(models.Model):
    name_college = models.CharField(max_length=100, verbose_name='Название колледжа')
    address_college = models.CharField(max_length=100, verbose_name='Адрес колледжа')
    date_of_foundation = models.DateTimeField(auto_now_add=True, verbose_name='Дата основания')
    filial_of_college = models.CharField(max_length=100, verbose_name='Филиал колледжа', blank=True)


class Gymnasium(models.Model):
    name_college = models.CharField(max_length=100, verbose_name='Название колледжа')
    address_college = models.CharField(max_length=100, verbose_name='Адрес колледжа')
    date_of_foundation = models.DateTimeField(auto_now_add=True, verbose_name='Дата основания')
    filial_of_college = models.CharField(max_length=100, verbose_name='Филиал колледжа', blank=True)

