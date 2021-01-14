from django.urls import path
from .views import StudentRegistrationApiView
#     CourseApiView,\
#     FacultyApiView,\
#     DirectionFacultyApiView,\
#     DoorRoomApiView,FLoorAPiVIew,Dorm_building
#
#
urlpatterns=[
    path('signup/', StudentRegistrationApiView.as_view()),
    # path('login/',LoginAPIView.as_view()),
#     path('course/', CourseApiView.as_view()),
#     path('faculty/',FacultyApiView.as_view()),
#     path('direction/', DirectionFacultyApiView.as_view()),
#     path('dooroom/',DoorRoomApiView.as_view()),
#     path('dorm_building/', Dorm_building.as_view()),
#     path('floor/', FLoorAPiVIew.as_view()),
#
]


from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('floor', FloorApiViewset, basename='floor')
# router.register('dorm_building', Dorm_buildingApiViewset, basename='dorm_building')
router.register('dorm_room', Dorm_roomApiViewset, basename='dorm_room')
router.register('direction',Dorm_roomApiViewset, basename='direction')
router.register('faculty', FacultyApiViewset, basename='faculty')
router.register('course', CourseApiViewset, basename='course')

urlpatterns=router.urls