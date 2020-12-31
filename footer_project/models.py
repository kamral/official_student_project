from django.db import models

# Create your models here.



class AboutUs(models.Model):

    title=models.CharField(max_length=100)
    body=models.TextField(verbose_name='Содержимое текста')
    date_of_foundation=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class  Contacts(models.Model):
    title=models.CharField(max_length=100)
    ceo_manager=models.CharField(max_length=100, verbose_name='Директор компании')
    backend_developer=models.CharField(max_length=100,verbose_name='Бек разработчик')
    frontent_developer=models.CharField(max_length=100, verbose_name='Фронт разработчик')
    support_service=models.CharField(max_length=100,verbose_name='Служба поддержки')

    def __str__(self):
        return self.title


class AboutCompany(models.Model):
    about_us=models.ForeignKey(AboutUs, on_delete=models.CASCADE,
                               verbose_name='О нас', blank=True)
    contacts=models.ForeignKey(Contacts,on_delete=models.CASCADE,
                               verbose_name='Контакты', blank=True)


class StudentHelpInformation(models.Model):
    title=models.CharField(max_length=100,verbose_name='Заголовок')
    body=models.TextField(verbose_name='Текст')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class AbiturientHelpInformation(models.Model):
    title=models.CharField(max_length=100,verbose_name='Заголовок')
    body=models.TextField(verbose_name='Текст')
    created_at=models.DateTimeField(auto_now_add=True)


class Oportunities(models.Model):
    student_information=models.ForeignKey(StudentHelpInformation,
                                          on_delete=models.CASCADE,
                                          verbose_name='Информация для студентов')
    abiturient_information=models.ForeignKey(AbiturientHelpInformation,
                                             on_delete=models.CASCADE,
                                             verbose_name='Информация для абитуриентов')

    def __str__(self):
        return self.title

class Ourpartners(models.Model):
    name=models.CharField(max_length=100,verbose_name='Имя партнера')


    def __str__(self):
        return self.name



