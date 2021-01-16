from django.urls import path
from .views import index,\
    get_education_category,get_education_detail,\
    get_dorm_building_detail
    # add_education_system,
from .views import Add_education_system

urlpatterns=[
    path('',index, name='home'),

    path('category_education/<int:pk>/',get_education_category,
    name='category_educations'),


    path('education/<int:pk>/', get_education_detail,
         name='education_detail'),
    ############################################################
    ###########################################################
    # path('education/add_education_system/', add_education_system,
    #      name='add_education_system'),
    path('education/add_education_system/', Add_education_system.as_view(),
         name='add_education_system'),
    path('dorm_building/<int:pk>/',get_dorm_building_detail,
         name='dorm_building')

]