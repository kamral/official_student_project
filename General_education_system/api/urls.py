# from django.urls import path
# from .views import CategoryApiView,\
#     GeneralEducationApiView,GeneralUpdateApiView
#
#
# urlpatterns=[
#     path('category_api/',CategoryApiView.as_view()),
#     path('category_api/<int:pk>/', CategoryApiView.as_view()),
#     path('general_education_api/', GeneralEducationApiView.as_view()),
#     path('general_education_api/<int:pk>/', GeneralUpdateApiView.as_view()),
#
# ]



from .views import CategoryEducationApiViewset,GeneralEducationSystemViewset
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('general_education_system',GeneralEducationSystemViewset, basename='general_education_system')
router.register('category_education', CategoryEducationApiViewset, basename='category_education')
urlpatterns=router.urls