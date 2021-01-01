from django.urls import path
from .view import \
    AboutUsApiView,\
    AboutUsUpdateApiView,\
    ContactApiView,\
    ContactUpdateApiView,\
    AboutCompanyApiView,\
    AboutCompanyUpdateApiView,\
    AbiturientInformationApiView,\
    AbiturientInformationUpdateApiView,\
    OportunitiesApiView,\
    OportunitiesUpdateApiView,OurpartnersApiView,OurpartnersUpdateApiView


urlpatterns=[
    path('about_us_company/',AboutUsApiView.as_view()),
    path('about_us_company/<int:pk>/', AboutUsUpdateApiView.as_view()),
    path('contacts/',ContactApiView.as_view()),
    path('contacts/<int:pk>/',ContactUpdateApiView.as_view()),
    path('about_company/',AboutCompanyApiView.as_view()),
    path('about_company/<int:pk>/',AboutCompanyUpdateApiView.as_view()),
    path('abiturient_help_information/',AbiturientInformationApiView.as_view()),
    path('abiturient_help_information/<int:pk>/',AbiturientInformationUpdateApiView.as_view()),
    path('oportunities/', OportunitiesApiView.as_view()),
    path('oportunities/<int:pk>/', OportunitiesUpdateApiView.as_view()),
    path('ourpartners/', OurpartnersApiView.as_view()),
    path('ourpartners/<int:pk>/', OurpartnersUpdateApiView.as_view())

]