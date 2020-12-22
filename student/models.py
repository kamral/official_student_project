from django.db import models
from user.models import User
# Create your models here.

class PhoneNumber(models.Model):
    phone_number=models.PositiveIntegerField(null=True,blank=True)



    class Meta:
        verbose_name='Номер телефона'
        verbose_name_plural='Номера телефонов'

class Course(models.Model):
    kurs_number=models.PositiveIntegerField(null=True, blank=True)



    class Meta:
        verbose_name='Курс'
        verbose_name_plural='Курсы'

class Faculty(models.Model):
    faculty_number=models.CharField(max_length=100)

    class Meta:
        verbose_name='Факультет'
        verbose_name_plural='Факультеты'

class Direction(models.Model):
    direction_name=models.CharField(max_length=100)


    class Meta:
        verbose_name='Направление'
        verbose_name_plural='Направления'

class Room(models.Model):
    room_number=models.PositiveIntegerField(null=True,blank=True)


    class Meta:
        verbose_name='Номер комнаты'
        verbose_name_plural='Номера комнат'


class student(models.Model):
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
    room = models.ForeignKey(Room, on_delete=models.CASCADE)





    class Meta:
        verbose_name='Студент'
        verbose_name_plural='Студенты'

        db_table='student'

