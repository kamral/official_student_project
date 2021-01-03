from .serialzers import \
    AboutCompanySerializers,\
    AboutCompany_CategorySerializers,\
    Ourpartners_categorySerializers,\
    OurpartnersSerializers,\
    OportunitiesSerializers,\
    Opportunities_category
from rest_framework.generics import\
    ListCreateAPIView,\
    RetrieveUpdateDestroyAPIView

from footer_project.models import \
    AboutCompany,\
    About_Company_Category,\
    Ourpartners,\
    Ourpartners_category,\
    Oportunities,\
    Opportunities_category

class AboutCompanyApiView(ListCreateAPIView):
    serializer_class = AboutCompanySerializers
    queryset = AboutCompany.objects.all()

class AboutCompanyUpdateApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = AboutCompany
    queryset = AboutCompany.objects.all()


class AboutCompanyCategoryApiView(ListCreateAPIView):
    serializer_class = AboutCompany_CategorySerializers
    queryset = About_Company_Category.objects.all()

class AboutCompanyCategoryUpdateApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = AboutCompany_CategorySerializers
    queryset = About_Company_Category.objects.all()

class OurpartnersApiView(ListCreateAPIView):
    serializer_class = OurpartnersSerializers
    queryset = Ourpartners.objects.all()

class OurpartnersUpdateApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = OurpartnersSerializers
    queryset = Ourpartners.objects.all()

class OurpartnersCategoryApiView(ListCreateAPIView):
    serializer_class = Ourpartners_categorySerializers
    queryset = Ourpartners_category.objects.all()

class OurpartnersCategoryUpdateApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = Ourpartners_categorySerializers
    queryset = Ourpartners_category.objects.all()


class OportunitiesApiView(ListCreateAPIView):
    serializer_class = OportunitiesSerializers
    queryset = Oportunities.objects.all()

class OportunitiesUpdateApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = OportunitiesSerializers
    queryset = Oportunities.objects.all()


class OportunitiesCategoryApiView(ListCreateAPIView):
    serializer_class = Opportunities_category
    queryset = Opportunities_category.objects.all()

class OportunitiesCategoryUpdateApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = Opportunities_category
    queryset = Opportunities_category.objects.all()

