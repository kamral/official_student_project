from django.urls import path
from .views import index

urlpatterns=[
    path('',index),
    # path('category_education/<int:pk>/',get_education_category, name='category')

]