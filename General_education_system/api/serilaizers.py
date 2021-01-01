# from General_education_system.models import \
#     University,\
#     Gymnasium,\
#     Colledge,\
#     Academic,BaseModel
#
#
# from student.models import *
#
#
# class BaseSerializers(serializers.ModelSerializer):
#     class Meta:
#         model=BaseModel
#         fields = ('image', 'name', 'address', 'date_of_foundation', 'filial')
#
#
# class UniversitySerializers(serializers.ModelSerializer):
#
#     class Meta(BaseSerializers.Meta):
#         model = University
#         fields = BaseSerializers.Meta.fields
#
#     def create(self, validated_data):
#         university = University.objects.create(**validated_data)
#         return university
#
# class GymnasuimSerializers(serializers.ModelSerializer):
#
#
#     class Meta(BaseSerializers.Meta):
#        model = Gymnasium
#        fields = BaseSerializers.Meta.fields
#
#
#     def create(self, validated_data):
#         gymnasium = Gymnasium.objects.create(**validated_data)
#
#
# class ColledgeSerializers(serializers.ModelSerializer):
#
#     class Meta(BaseSerializers.Meta):
#         model=Colledge
#         fields = BaseSerializers.Meta.fields
#
#
#     def create(self, validated_data):
#         colledge=Colledge.objects.create(**validated_data)
#         return colledge
#
# class AcademicSerializers(serializers.ModelSerializer):
#
#
#     class Meta(BaseSerializers.Meta):
#         model = Academic
#         fields = BaseSerializers.Meta.fields
#
#     def create(self, validated_data):
#         academic = Academic.objects.create(**validated_data)
#         return academic

from rest_framework import serializers
from General_education_system.models import \
    General_education_system,\
    Category_education

class CategorySerializers(serializers.ModelSerializer):
    name=serializers.CharField()

    def create(self, validated_data):
        category_education=Category_education.objects.all()
        return category_education

    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.save()
        return instance




    class Meta:
        model=Category_education
        fields=('name',)





class GeneralEducationSystemSerializers(serializers.ModelSerializer):

    image=serializers.ImageField()
    name=serializers.CharField()
    address=serializers.CharField()
    date_of_foundation=serializers.DateTimeField()
    filial_of_foundation=serializers.CharField()
    history_of_university=serializers.CharField()
    category_education=serializers.PrimaryKeyRelatedField(queryset=Category_education.objects.all())

    def create(self, validated_data):
        general_education_system=General_education_system.objects.aLL()
        return general_education_system

    def update(self, instance, validated_data):
        instance.image=validated_data.get('image',instance.image)
        instance.name=validated_data.get('name',instance.name)
        instance.address=validated_data.get('address',instance.address)
        instance.date_of_foundation=validated_data.get('date_of_foundation',
                                                       instance.date_of_foundation)
        history_of_university=validated_data.get('history_of_university',
                                                 instance.history_of_university)
        instance.save()
        return instance

    class Meta:
        model=General_education_system
        fields=('name','image','address','date_of_foundation',
                'filial_of_foundation','history_of_university',
                'category_education')




























