from rest_framework import serializers
from footer_project.models import *



class AboutUsSerializers(serializers.ModelSerializer):
    title=serializers.CharField()
    body=serializers.CharField()
    date_of_foundation=serializers.DateTimeField()


    def create(self, validated_data):
        about_us=AboutUs.objects.all()
        return about_us

    def update(self, instance, validated_data):
        instance.title=validated_data.get('title',instance.title)
        instance.body=validated_data.get('body',instance.body)
        instance.date_of_foundation=validated_data.get('date_of_foundation',
                                                       instance.date_of_foundation)
        instance.save()
        return instance

    class Meta:
        model=AboutUs
        fields=('title','body','date_of_foundation')



class ContactsSerializers(serializers.ModelSerializer):

    title=serializers.CharField()
    ceo_manager=serializers.CharField()
    backend_developer=serializers.CharField()
    frontent_developer=serializers.CharField()
    support_service=serializers.CharField()

    def create(self, validated_data):
        contact=Contacts.objetcs.all()
        return contact

    def update(self, instance, validated_data):
        instance.title=validated_data.get('title',instance.title)
        instance.ceo_manager=validated_data.get('ceo_manager',instance.ceo_manager)
        instance.backend_developer=validated_data.get('backend_developer',instance.backend_developer)
        instance.frontent_developer=validated_data.get('frontent_developer',instance.frontent_developer)
        instance.support_service=validated_data.get('support_service',instance.support_service)
        instance.save()
        return instance

    class Meta:
        model=Contacts
        fields=('title','ceo_manager','backend_developer',
                'frontent_developer','support_service')




class AboutCompanySerializers(serializers.ModelSerializer):
    about_company=serializers.PrimaryKeyRelatedField(queryset=AboutCompany.objects.all())
    contacts=serializers.PrimaryKeyRelatedField(queryset=Contacts.objects.all())

    def create(self, validated_data):
        about_company=AboutCompany.objects.all()
        return about_company

    def update(self, instance, validated_data):
        instance.about_company=validated_data.get('about_company',instance.about_company)
        instance.contacts=validated_data.get('contacts',instance.contacts)

        class Meta:
            model=AboutCompany
            fields=('about_company','contacts',)

class StudentHelpInformation(models.Model):
    title=models.CharField(max_length=100,verbose_name='Заголовок')
    body=models.TextField(verbose_name='Текст')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class AbiturientHelpInformation(serializers.ModelSerializer):
    title=serializers.CharField()
    body=serializers.CharField()
    created_at=serializers.DateTimeField()

    def create(self, validated_data):
        abiturient_information=AbiturientHelpInformation.objects.all()
        return abiturient_information

    def update(self, instance, validated_data):
        instance.title=validated_data.get('title',instance.title)
        instance.body=validated_data.get('title',instance.created_at)


    class Meta:
        model=Ourpartners
        fields=('title','body','created_at',)


class OportunitiesSerializers(serializers.ModelSerializer):
    student_information=serializers.PrimaryKeyRelatedField(queryset=StudentHelpInformation.objects.all())
    abiturient_information=serializers.PrimaryKeyRelatedField(queryset=AboutUsSerializers.objects.all())

    def create(self, validated_data):
        ourpartners=Ourpartners.objects.all()
        return ourpartners



    def update(self, instance, validated_data):
        instance.student_information=validated_data.get('student_information')
        instance.abiturient_information=validated_data.get('abiturient_information')
        instance.save()
        return instance

    class Meta:
        model=Oportunities
        fields=('student_information','abiturient_information',)


class OurpartnersSerializers(serializers.ModelSerializer):
    name=serializers.CharField()

    def create(self, validated_data):
        ourpartners=Ourpartners.objects.all()
        return ourpartners

    def update(self, instance, validated_data):
        instance.name=validated_data.get('name', instance.name)
        instance.save()
        return instance

    class Meta:
        model=Ourpartners
        fields=('name',)