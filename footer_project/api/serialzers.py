from rest_framework import serializers
from footer_project.models import *





class AboutCompanySerializers(serializers.ModelSerializer):


    category=serializers.PrimaryKeyRelatedField(queryset=About_Company_Category.objects.all())


    def create(self, validated_data):
        return AboutCompany.objects.all()




    class Meta:
        model=AboutCompany
        fields=('title','body','date_of_foundation','ceo_manager',
                'backend_developer','frontent_developer','support_service',
                'category',)



class AboutCompany_CategorySerializers(serializers.ModelSerializer):
    name=serializers.CharField()

    def create(self, validated_data):
        return About_Company_Category.objects.all()

    class Meta:
        model=About_Company_Category
        fields=('name',)


class OportunitiesSerializers(serializers.ModelSerializer):
    title = serializers.CharField()
    question = serializers.CharField()
    answer = serializers.CharField()
    body = serializers.CharField()
    created_at = serializers.DateTimeField()
    category = serializers.PrimaryKeyRelatedField(queryset=Opportunities_category.objects.all())


    def create(self, validated_data):
        return Oportunities.objects.all()

    class Meta:
        model=Oportunities
        fields=('title','question','answer','body','created_at',
                'created_at','category')


class Oportunities_categorySerializers(serializers.ModelSerializer):
    name=serializers.CharField()

    def create(self, validated_data):
        return Oportunities.objects.all()

    class Meta:
        model=Oportunities
        fields=('name',)


class OurpartnersSerializers(serializers.ModelSerializer):
    name=serializers.CharField()
    address=serializers.CharField()
    category=serializers.PrimaryKeyRelatedField(queryset=Ourpartners.objects.all())

    def create(self, validated_data):
        return Ourpartners.objects.all()

    class Meta:
        model=Ourpartners
        fields=('name','address','category')



class Ourpartners_categorySerializers(serializers.ModelSerializer):
    name=serializers.CharField()

    def create(self, validated_data):
        return Ourpartners.objects.all()

    class Meta:
        model=Ourpartners
        fields=('name',)
