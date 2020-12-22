from django.shortcuts import render
from .serializers import StudentRegisterSerializer
# Create your views here.

from student.models import student
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response


class StudentRegistrationApiView(CreateAPIView):
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