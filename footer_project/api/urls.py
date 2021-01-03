from django.urls import path
from .view import AboutCompanyApiView,\
    AboutCompanyUpdateApiView,\
    AboutCompanyCategoryApiView,\
    AboutCompanyCategoryUpdateApiView,\
    OurpartnersApiView,\
    OurpartnersUpdateApiView,\
    OportunitiesUpdateApiView,\
    OportunitiesApiView

urlpatterns=[
    path('about_company/',AboutCompanyApiView.as_view()),
    path('about_company/<int:pk>/', AboutCompanyUpdateApiView.as_view()),
    path('about_company_category/',AboutCompanyCategoryApiView.as_view()),
    path('about_company_category/<int:pk>/',AboutCompanyCategoryUpdateApiView.as_view()),
    path('ourpartners/',OurpartnersApiView.as_view()),
    path('ourpartners/<int:pk>/',OurpartnersUpdateApiView.as_view()),
    path('oportunities/',OportunitiesApiView.as_view()),
    path('oportunities/<int:pk>/',OportunitiesUpdateApiView.as_view()),

]