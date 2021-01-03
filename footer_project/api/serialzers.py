from rest_framework import serializers
from footer_project.models import *





class AboutCompanySerializers(serializers.ModelSerializer):
    title=serializers.CharField()
    body=serializers.CharField()
    date_of_foundation=serializers.DateTimeField()
    ceo_manager=serializers.CharField()
    backend_developer=serializers.CharField()
    frontent_developer=serializers.CharField()
    support_service=serializers.CharField()
    category=serializers.PrimaryKeyRelatedField(queryset=About_Company_Category.objects.all())


    def create(self, validated_data):
        return AboutCompany.objects.all()


    class Meta:
        mdoel=AboutCompany
        fields=('title','body','date_of_foundation','ceo_manager',
                'backend_manager','frontent_manager','support_service',
                'category')


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


class Ourpartners_category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Ourpartners_categorySerializers(serializers.ModelSerializer):
    name=serializers.CharField()

    def create(self, validated_data):
        return Ourpartners.objects.all()

    class Meta:
        model=Ourpartners
        fields=('name',)
