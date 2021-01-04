from django.urls import path
from .views import index,get_education_category

urlpatterns=[
    path('',index, name='home'),
    path('category_education/<int:pk>/',get_education_category,
    name='category_educations')



]