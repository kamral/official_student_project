from django.urls import path,include
from .view import AboutCompanyApiView,\
    AboutCompanyUpdateApiView,\
    AboutCompanyCategoryApiView,\
    AboutCompanyCategoryUpdateApiView,\
    OurpartnersApiView,\
    OurpartnersUpdateApiView,\
    OportunitiesUpdateApiView,\
    OportunitiesApiView
from rest_framework import routers

# routers=routers.DefaultRouter()
# routers.register('home', HomeApiView)

urlpatterns=[

    # path('', include(routers.urls)),
    path('about_company/',AboutCompanyApiView.as_view(),name='home'),
    path('about_company/<int:pk>/', AboutCompanyUpdateApiView.as_view()),
    path('about_company_category/',AboutCompanyCategoryApiView.as_view()),
    path('about_company_category/<int:pk>/',AboutCompanyCategoryUpdateApiView.as_view()),
    path('ourpartners/',OurpartnersApiView.as_view()),
    path('ourpartners/<int:pk>/',OurpartnersUpdateApiView.as_view()),
    path('oportunities/',OportunitiesApiView.as_view()),
    path('oportunities/<int:pk>/',OportunitiesUpdateApiView.as_view())

]