# from collections import OrderedDict
#
# from rest_framework.pagination import PageNumberPagination
# from rest_framework.response import Response
#
# from .serilaizers import \
#     UniversitySerializers
#     # ColledgeSerializers,\
#     # GymnasuimSerializers,\
#     # AcademicSerializers
# from rest_framework.generics import\
#     ListCreateAPIView,\
#     RetrieveUpdateDestroyAPIView
# from General_education_system.models import University,\
#     Colledge,\
#     Gymnasium,\
#     Academic
#
# class UniversityPagination(PageNumberPagination):
#     page_size = 2
#     page_query_param = 'page_size'
#     max_page_size = 10
#
#     def get_paginated_response(self, data):
#         return Response(OrderedDict([
#             ('колчество объектов', self.page.paginator.count),
#             ('следующий', self.get_next_link()),
#             ('предыдущий', self.get_previous_link()),
#             ('результат', data)
#         ]))
#
#
# class UniversityApiView(ListCreateAPIView):
#     queryset = University.objects.all()
#     serializer_class = UniversitySerializers
#     pagination_class = UniversityPagination