from django.urls import path
from .views import StudentRegistrationApiView,\
    CourseApiView,\
    FacultyApiView,\
    DirectionFacultyApiView,\
    DoorRoomApiView,UniversityApiView


urlpatterns=[
    path('signup/', StudentRegistrationApiView.as_view()),
    # path('login/',LoginAPIView.as_view()),
    path('course/', CourseApiView.as_view()),
    path('faculty/',FacultyApiView.as_view()),
    path('direction/', DirectionFacultyApiView.as_view()),
    path('dooroom/',DoorRoomApiView.as_view()),
    path('university/',UniversityApiView.as_view())
]