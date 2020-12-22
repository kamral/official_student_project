from django.urls import path
from .views import StudentRegistrationApiView


urlpatterns=[
    path('signup/', StudentRegistrationApiView.as_view())
]