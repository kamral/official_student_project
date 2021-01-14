from django.shortcuts import render
from .serializers import *
# Create your views here.
from General_education_system.models import *
from student.models import *
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from collections import OrderedDict
from rest_framework.viewsets import ModelViewSet

class StudentRegistrationApiView(generics.CreateAPIView):
    serializer_class = StudentRegisterSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code=status.HTTP_201_CREATED
        response={
            'success':'True',
            'status code':status_code,
            'message':'Пользователь успешно зарегистрированн'
        }

        return Response(response, status=status_code)





#
# class CourseApiView(generics.ListCreateAPIView):
#     serializer_class = CourseSerializers
#     queryset = Course.objects.all()

class CourseApiViewset(ModelViewSet):
    serializer_class = CourseSerializers
    queryset = Course.objects.all()

#
# class FacultyApiView(generics.ListCreateAPIView):
#     serializer_class = FacultySerializers
#     queryset = Faculty.objects.all()


class FacultyApiViewset(ModelViewSet):
    serializer_class = FacultySerializers
    queryset = Faculty.objects.all()


# создаем пагинаию на уровне модели
class DirectionPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page_size'
    max_page_size = 10

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('колчество объектов', self.page.paginator.count),
            ('следующий', self.get_next_link()),
            ('предыдущий', self.get_previous_link()),
            ('результат', data)
        ]))



# class DirectionFacultyApiView(generics.ListCreateAPIView):
#     serializer_class = DirectionSerializers
#     queryset = Direction.objects.all()
#     pagination_class=DirectionPagination


class DirectionFacultyAPiViewset(ModelViewSet):
    serializer_class = DirectionSerializers
    queryset = Direction.objects.all()
    pagination_class = DirectionPagination


# class FLoorAPiVIew(generics.ListCreateAPIView):
#     serializer_class = FLoorSerializers
#     queryset = Floor.objects.all()


class FloorApiViewset(ModelViewSet):
    serializer_class = FLoorSerializers
    queryset = Floor.objects.all()


# class Dorm_buildingApiView(generics.ListCreateAPIView):
#     serializer_class = Dorm_buildingSerializers
#     queryset = Dorm_building.objects.all()

# class Dorm_buildingApiViewset(ModelViewSet):
#     serializer_class = Dorm_buildingSerializers
#     queryset = Dorm_building.objects.all()




# class DoorRoomApiView(generics.ListCreateAPIView):
#     serializer_class = Dorm_roomSerializers
#     queryset = Dorm_room.objects.all()

class Dorm_roomApiViewset(ModelViewSet):
    serializer_class = Dorm_roomSerializers
    queryset = Dorm_room.objects.all()
