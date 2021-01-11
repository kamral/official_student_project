from django.urls import path
from .views import StudentRegistrationApiView,\
    CourseApiView,\
    FacultyApiView,\
    DirectionFacultyApiView,\
    DoorRoomApiView,FLoorAPiVIew,Dorm_building


urlpatterns=[
    path('signup/', StudentRegistrationApiView.as_view()),
    # path('login/',LoginAPIView.as_view()),
    path('course/', CourseApiView.as_view()),
    path('faculty/',FacultyApiView.as_view()),
    path('direction/', DirectionFacultyApiView.as_view()),
    path('dooroom/',DoorRoomApiView.as_view()),
    path('dorm_building/', Dorm_building.as_view()),
    path('floor/', FLoorAPiVIew.as_view()),

]