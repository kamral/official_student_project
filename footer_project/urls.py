from django.urls import path
from .views import home,\
    get_about_company_category_footer,\
    get_about_company_category_footer_contacts


urlpatterns=[
    path('',home),
    path('about_us/<str:pk>/', get_about_company_category_footer,
         name='about_us'),
    path('contacts/<int:pk>/', get_about_company_category_footer_contacts,
         name='contacts'),

]
