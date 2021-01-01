from .serialzers import \
    AboutUsSerializers,\
    ContactsSerializers,\
    AboutCompanySerializers,\
    StudentHelpInformationSerializers,\
    AbiturientHelpInformationSerializers,\
    OportunitiesSerializers,\
    OurpartnersSerializers
from rest_framework.generics import\
    ListCreateAPIView,\
    RetrieveUpdateDestroyAPIView

from footer_project.models import\
    AboutUs,\
    Contacts,\
    AboutCompany,\
    StudentHelpInformation,\
    AbiturientHelpInformation,\
    Oportunities,\
    Ourpartners

class AboutUsApiView(ListCreateAPIView):
    serializer_class = AboutUsSerializers
    queryset = AboutUs.objects.all()

class AboutUsUpdateApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = AboutUsSerializers
    queryset = AboutUs.objects.all()


class ContactApiView(ListCreateAPIView):
    serializer_class = ContactsSerializers
    queryset = Contacts.objects.all()

class ContactUpdateApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = ContactsSerializers
    queryset = Contacts.objects.all()


class AboutCompanyApiView(ListCreateAPIView):
    serializer_class = AboutCompanySerializers
    queryset = AboutCompany.objects.all()

class AboutCompanyUpdateApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = AboutCompanySerializers
    queryset = AboutCompany.objects.all()


class StudentHelpInformationApiView(ListCreateAPIView):
    serializer_class = StudentHelpInformationSerializers
    queryset = StudentHelpInformation.objects.all()

class StudentHelpInformationUpdateApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = StudentHelpInformationSerializers
    queryset = StudentHelpInformation.objects.all()


class AbiturientInformationApiView(ListCreateAPIView):
    serializer_class = AbiturientHelpInformationSerializers
    queryset = AbiturientHelpInformation.objects.all()


class AbiturientInformationUpdateApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = AbiturientHelpInformationSerializers
    queryset = AbiturientHelpInformation.objects.all()


class OportunitiesApiView(ListCreateAPIView):
    serializer_class = OportunitiesSerializers
    queryset = Oportunities.objects.all()

class OportunitiesUpdateApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = OportunitiesSerializers
    queryset = Oportunities.objects.all()


class OurpartnersApiView(ListCreateAPIView):
    serializer_class = OportunitiesSerializers
    queryset = Oportunities.objects.all()

class OurpartnersUpdateApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = OportunitiesSerializers
    queryset = Oportunities.objects.all()