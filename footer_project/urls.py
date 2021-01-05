from django.urls import path
from .views import home, \
    get_about_company_category_footer,\
    get_opportunities_footer,get_ourpartners

urlpatterns=[
    path('',home),
    path('about_company/<int:pk>/', get_about_company_category_footer,
         name='about_company'),
    path('oportunities/<int:pk>/', get_opportunities_footer,
         name='oportunities'),
    path('ourpartners/<int:pk>/', get_ourpartners,
         name='ourpartners'),


]
