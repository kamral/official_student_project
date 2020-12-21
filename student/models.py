from django.db import models
from user.models import User
# Create your models here.

class PhoneNmuber(models.Model):
    phone_number=models.PositiveIntegerField(null=True,blank=True)
    def __str__(self):
        return self.phone_number


    class Meta:
        verbose_name='Номер телефона'
        verbose_name_plural='Номера телефонов'

class Course(models.Model):
    kurs_number=models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.kurs


    class Meta:
        verbose_name='Курс'
        verbose_name_plural='Курсы'

class Faculty(models.Model):
    faculty_number=models.PositiveIntegerField(null=True,blank=True)

    def __str__(self):
        return self.faculty_number


    class Meta:
        verbose_name='Факультет'
        verbose_name_plural='Факультеты'

class Direction(models.Model):
    direction_name=models.CharField(max_length=100)

    def __str__(self):
        return self.direction_name


    class Meta:
        verbose_name='Направление'
        verbose_name_plural='Направления'

class Room(models.Model):
    room_number=models.PositiveIntegerField(null=True,blank=True)

    def __str__(self):
        return self.room_number


    class Meta:
        verbose_name='Номер комнаты'
        verbose_name_plural='Номера комнат'


class student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    second_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    telephone_number = models.ForeignKey(PhoneNmuber, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)


    def __str__(self):
        return self.user


    class Meta:
        verbose_name='Студент'
        verbose_name_plural='Студенты'



