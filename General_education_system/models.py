from django.db import models
# Create your models here.
from PIL import Image
from student.models import *



class BaseModel(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date_of_foundation = models.DateTimeField(auto_now_add=True, )
    filial = models.CharField(max_length=100, verbose_name='Филиал университета', blank=True)
    # course=models.ForeignKey(Course,on_delete=models.CASCADE)
    # Faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE)
    # direction=models.ForeignKey(Direction,on_delete=models.CASCADE)
    # Dorm_room=models.ForeignKey(Dorm_room,on_delete=models.CASCADE)




class University(BaseModel):
    pass

class Colledge(models.Model):
    pass

class Academic(models.Model):
    pass

class Gymnasium(models.Model):
    pass