from rest_framework import serializers
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
