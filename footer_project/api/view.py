from .serialzers import \
    AboutCompanySerializers,\
    AboutCompany_CategorySerializers,\
    Ourpartners_categorySerializers,\
    OurpartnersSerializers,\
    OportunitiesSerializers,\
    Opportunities_category
from rest_framework.generics import\
    ListCreateAPIView
#     RetrieveUpdateDestroyAPIView
from rest_framework import viewsets

from footer_project.models import \
    AboutCompany,\
    About_Company_Category,\
    Ourpartners,\
    Ourpartners_category,\
    Oportunities,\
    Opportunities_category

from rest_framework.viewsets import ModelViewSet



class AboutCompanyApiView(ListCreateAPIView):
    serializer_class = AboutCompanySerializers
    queryset = AboutCompany.objects.all()



# class AboutCompanyUpdateApiView(RetrieveUpdateDestroyAPIView):
#     serializer_class = AboutCompanySerializers
#     queryset = AboutCompany.objects.all()


class AboutCompanyViewsets(ModelViewSet):
    queryset = AboutCompany.objects.all()
    serializer_class = AboutCompanySerializers







# class AboutCompanyCategoryApiView(ListCreateAPIView):
#     serializer_class = AboutCompany_CategorySerializers
#     queryset = About_Company_Category.objects.all()
#
# class AboutCompanyCategoryUpdateApiView(RetrieveUpdateDestroyAPIView):
#     serializer_class = AboutCompany_CategorySerializers
#     queryset = About_Company_Category.objects.all()


class AboutCompanyCategoryViewsets(ModelViewSet):
    queryset = About_Company_Category.objects.all()
    serializer_class = AboutCompany_CategorySerializers


#
# class OurpartnersApiView(ListCreateAPIView):
#     serializer_class = OurpartnersSerializers
#     queryset = Ourpartners.objects.all()
#
# class OurpartnersUpdateApiView(RetrieveUpdateDestroyAPIView):
#     serializer_class = OurpartnersSerializers
#     queryset = Ourpartners.objects.all()
#

class OurpartnersViewsets(ModelViewSet):
    queryset = Ourpartners.objects.all()
    serializer_class = OurpartnersSerializers


# class OurpartnersCategoryApiView(ListCreateAPIView):
#     serializer_class = Ourpartners_categorySerializers
#     queryset = Ourpartners_category.objects.all()
#
# class OurpartnersCategoryUpdateApiView(RetrieveUpdateDestroyAPIView):
#     serializer_class = Ourpartners_categorySerializers
#     queryset = Ourpartners_category.objects.all()
#


class OurpartnersCategoryViewsets(ModelViewSet):
    queryset = Ourpartners_category.objects.all()
    serializer_class = OurpartnersSerializers

#
# class OportunitiesApiView(ListCreateAPIView):
#     serializer_class = OportunitiesSerializers
#     queryset = Oportunities.objects.all()
#
# class OportunitiesUpdateApiView(RetrieveUpdateDestroyAPIView):
#     serializer_class = OportunitiesSerializers
#     queryset = Oportunities.objects.all()
#
#

class OportunitiesViewsets(ModelViewSet):
    queryset = Oportunities.objects.all()
    serializer_class = OportunitiesSerializers



# class OportunitiesCategoryApiView(ListCreateAPIView):
#     serializer_class = Opportunities_category
#     queryset = Opportunities_category.objects.all()
#
# class OportunitiesCategoryUpdateApiView(RetrieveUpdateDestroyAPIView):
#     serializer_class = Opportunities_category
#     queryset = Opportunities_category.objects.all()
#

class OportunitiesCategory(ModelViewSet):
    serializer_class = Opportunities_category
    queryset = Opportunities_category.objects.all()
