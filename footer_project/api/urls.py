# from django.urls import path,include
# from .view import AboutCompanyApiView,\
#     AboutCompanyUpdateApiView,\
#     AboutCompanyCategoryApiView,\
#     AboutCompanyCategoryUpdateApiView,\
#     OurpartnersApiView,\
#     OurpartnersUpdateApiView,\
#     OportunitiesUpdateApiView,\
#     OportunitiesApiView
# from rest_framework import routers
#
# # routers=routers.DefaultRouter()
# # routers.register('home', HomeApiView)
#
# urlpatterns=[
#
#     # path('', include(routers.urls)),
#     path('about_company/',AboutCompanyApiView.as_view(),name='home'),
#     path('about_company/<int:pk>/', AboutCompanyUpdateApiView.as_view()),
#     path('about_company_category/',AboutCompanyCategoryApiView.as_view()),
#     path('about_company_category/<int:pk>/',AboutCompanyCategoryUpdateApiView.as_view()),
#     path('ourpartners/',OurpartnersApiView.as_view()),
#     path('ourpartners/<int:pk>/',OurpartnersUpdateApiView.as_view()),
#     path('oportunities/',OportunitiesApiView.as_view()),
#     path('oportunities/<int:pk>/',OportunitiesUpdateApiView.as_view())
#
# ]



from .view import *
from  rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('about_company',AboutCompanyViewsets, basename='about_company')
router.register('about_company_category', AboutCompanyViewsets, basename='about_company_category')
router.register('ourpartners', OurpartnersViewsets, basename='ourpartners')
router.register('ourpartners_category',OurpartnersCategoryViewsets, basename='ourpartners_category')
router.register('oportunities', OportunitiesViewsets, basename='oportunities')
router.register('oportunities_category', OurpartnersCategoryViewsets, basename='oportunities_category')
urlpatterns=router.urls

