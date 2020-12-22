from django.db import models

# Create your models here.



class AboutUs(models.Model):

    name_company=models.CharField(max_length=100,verbose_name='Название компании')
    body=models.TimeField(verbose_name='Содержимое текста')
    date_of_foundation=models.DateTimeField(auto_now_add=True)


class  Contacts(models.Model):
    ceo_manager=models.CharField(max_length=100, verbose_name='Директор компании')
    backend_developer=models.CharField(max_length=100,verbose_name='Бек разработчик')
    frontent_developer=models.CharField(max_length=100, verbose_name='Фронт разработчик')
    support_service=models.CharField(max_length=100,verbose_name='Служба поддержки')



class StudentHelpInformation(models.Model):
    title=models.CharField(max_length=100,verbose_name='Заголовок')
    body=models.TextField(verbose_name='Текст')
    created_at=models.DateTimeField(auto_now_add=True)

class AbiturientHelpInformation(models.Model):
    title=models.CharField(max_length=100,verbose_name='Заголовок')
    body=models.TextField(verbose_name='Текст')
    created_at=models.DateTimeField(auto_now_add=True)


class Ourpartners(models.Model):
    name=models.CharField(max_length=100,verbose_name='Имя партнера')



