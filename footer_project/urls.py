from django.urls import path
# from .views import get_ourpartners
    # home, \
    # get_opportunities_footer,
    # get_about_company_category_footer,\

from .views import \
    Home,\
    AboutCompanyCategoryFooter,\
    Oportunities_footer,Ourpartners_footer

urlpatterns=[
    # path('', home),
    path('class/home/',Home.as_view(), name='home'),
    # path('about_company/<int:pk>/', get_about_company_category_footer,
    #      name='about_company'),
    ##########################################################
    ##########################################################

    path('about_company/<int:pk>/',AboutCompanyCategoryFooter.as_view(),
         name='about_company'),
    # path('oportunities/<int:pk>/', get_opportunities_footer,
    #      name='oportunities'),

    path('oportunities/<int:pk>/', Oportunities_footer.as_view(),
         name='oportunities'),
    #############################################################
    #############################################################

    path('ourpartners/<int:pk>/', Ourpartners_footer.as_view(),
         name='ourpartners'),


]
