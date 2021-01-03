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
        instance.date_of_foundation=validated_data.get('date_of_foundation',instance.date_of_foundation)
        instance.save()
        return instance

    class Meta:
        model=AboutUs
        fields=('title','body','date_of_foundation',)



class ContactsSerializers(serializers.ModelSerializer):

    title=serializers.CharField()
    ceo_manager=serializers.CharField()
    backend_developer=serializers.CharField()
    frontent_developer=serializers.CharField()
    support_service=serializers.CharField()

    def create(self, validated_data):
        contact=Contacts.objects.all()
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



class QuestionSerializers(serializers.ModelSerializer):
    title=serializers.CharField()
    body=serializers.CharField()
    created_at=serializers.DateTimeField()

    def create(self, validated_data):
        student_help_information=Questions.objects.all()
        return student_help_information

    def update(self, instance, validated_data):
        instance.title=validated_data.get('title', instance.title)
        instance.body=validated_data.get('body', instance.body)
        instance.created_at=validated_data.get('created_at', instance.created_at)
        instance.save()
        return instance

    class Meta:
        model=Questions
        fields=('title','body','created_at')



class AnswerSerializers(serializers.ModelSerializer):
    title=serializers.CharField()
    body=serializers.CharField()
    created_at=serializers.DateTimeField()

    def create(self, validated_data):
        abiturient_information=Answers.objects.all()
        return abiturient_information

    def update(self, instance, validated_data):
        instance.title=validated_data.get('title',instance.title)
        instance.body=validated_data.get('title',instance.created_at)


    class Meta:
        model=Answers
        fields=('title','body','created_at',)



class OportunitiesSerializers(serializers.ModelSerializer):
    title=serializers.CharField()
    question=serializers.PrimaryKeyRelatedField(queryset=Questions.objects.all())
    answer=serializers.PrimaryKeyRelatedField(queryset=Answers.objects.all())

    def create(self, validated_data):
        oportunities=Oportunities.objects.all()
        return oportunities



    def update(self, instance, validated_data):
        instance.question=validated_data.get('question')
        instance.answer=validated_data.get('answer')
        instance.title=validated_data.get('title')
        instance.save()
        return instance

    class Meta:
        model=Oportunities
        fields=('title','answer','question')


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