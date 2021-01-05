from django.db import models
from django.urls import reverse
# Create your models here.



class AboutCompany(models.Model):

    title=models.CharField(max_length=100)
    body=models.TextField(verbose_name='Содержимое текста',blank=True)
    date_of_foundation=models.DateTimeField(auto_now_add=True)
    ceo_manager = models.CharField(max_length=100,
                                   verbose_name='Директор компании',blank=True)
    backend_developer = models.CharField(max_length=100,
                                         verbose_name='Бек разработчик',blank=True)
    frontent_developer = models.CharField(max_length=100,
                                          verbose_name='Фронт разработчик',blank=True)
    support_service = models.CharField(max_length=100,
                                       verbose_name='Служба поддержки',blank=True)
    category=models.ForeignKey('About_Company_Category',on_delete=models.CASCADE)
    def __str__(self):
        return self.title

# В данной категории будут у нас - О нас, Контакты
class About_Company_Category(models.Model):
    name=models.CharField(max_length=100, verbose_name='Имя ')

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id'})

    def __str__(self):
        return self.name



class Oportunities(models.Model):
    title=models.CharField(max_length=100)
    question=models.CharField(max_length=100,verbose_name='Вопрос')
    answer=models.CharField(max_length=100,verbose_name='Ответ')
    body = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True)
    category=models.ForeignKey('Opportunities_category',on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Opportunities_category(models.Model):
    name=models.CharField(max_length=100,verbose_name='Имя')


    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id'})

    def __str__(self):
        return self.name

class Ourpartners(models.Model):
    name=models.CharField(max_length=100,verbose_name='Имя партнера')
    address=models.CharField(max_length=100, verbose_name='Адрес')
    category=models.ForeignKey('Ourpartners_category',on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Ourpartners_category(models.Model):
    name=models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id'})

    def __str__(self):
        return self.name





