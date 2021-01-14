from django.db import models
from django.urls import reverse

from user.models import User
# Create your models here.
from PIL import Image




class Course(models.Model):
    kurs_number=models.PositiveIntegerField(null=True, blank=True)


    class Meta:
        verbose_name='Курс'
        verbose_name_plural='Курсы'


    def __str__(self):
        return self.kurs_number

class Faculty(models.Model):
    faculty_number=models.CharField(max_length=100)

    class Meta:
        verbose_name='Факультет'
        verbose_name_plural='Факультеты'

    def __str__(self):
        return self.faculty_number

class Direction(models.Model):
    direction_name=models.CharField(max_length=100)

    def __str__(self):
        return self.direction_name

class Room(models.Model):
    room_number=models.PositiveIntegerField(null=True,blank=True)
    student_name=models.CharField(max_length=100)
    # student_name=models.ForeignKey('Student',on_delete=models.CASCADE)
    student_photo=models.ImageField(verbose_name='Фото студента')

    def __str__(self):
        return self.room_number

    class Meta:
        verbose_name='Номер комнаты'
        verbose_name_plural='Номера комнат'


class Dorm_building(models.Model):
    number_building = models.CharField(max_length=100)
    dorm_room=models.ForeignKey('Dorm_room',on_delete=models.CASCADE)



    def __str__(self):
        return self.number_building

class Floor(models.Model):
    number_floor = models.CharField(max_length=100)
    dorm_bulding = models.ForeignKey(Dorm_building,on_delete=models.CASCADE)




    def __str__(self):
        return self.number_floor

class Dorm_room(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название общежития')
    address = models.CharField(max_length=100,verbose_name='Адрес')



    def __str__(self):
        return self.title

class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,
                              related_name='student')
    first_name=models.CharField(max_length=100)
    second_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    telephone_number = models.CharField(max_length=100, unique=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    dorm_room=models.ForeignKey(Dorm_room,on_delete=models.CASCADE)


    def __str__(self):
        return self.user


    class Meta:
        verbose_name='Студент'
        verbose_name_plural='Студенты'

        db_table='student'

