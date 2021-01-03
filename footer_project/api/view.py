from .serialzers import \
    AboutUsSerializers,\
    ContactsSerializers,\
    AboutCompanySerializers,\
    QuestionSerializers,\
    AnswerSerializers,\
    OportunitiesSerializers,\
    OurpartnersSerializers
from rest_framework.generics import\
    ListCreateAPIView,\
    RetrieveUpdateDestroyAPIView

from footer_project.models import\
    AboutUs,\
    Contacts,\
    AboutCompany,\
    Questions,\
    Answers,\
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


class QuestionApiView(ListCreateAPIView):
    serializer_class = QuestionSerializers
    queryset = Questions.objects.all()

class QuestionUpdateApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializers
    queryset = Questions.objects.all()


class AnswerApiView(ListCreateAPIView):
    serializer_class = AnswerSerializers
    queryset = Answers.objects.all()


class AnswerUpdateApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = AnswerSerializers
    queryset = Answers.objects.all()


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