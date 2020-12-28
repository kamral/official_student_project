from rest_framework import serializers
from General_education_system.models import \
    University,\
    Gymnasium,\
    Colledge,\
    Academic,BaseModel


from student.models import *


class BaseSerializers(serializers.ModelSerializer):
    class Meta:
        model=BaseModel
        fields = ('image', 'name', 'address', 'date_of_foundation', 'filial',
                  'course', 'Faculty', 'direction', 'Dorm_room')


class UniversitySerializers(serializers.ModelSerializer):

    class Meta(BaseSerializers.Meta):
        model = University
        fields = BaseSerializers.Meta.fields

    def create(self, validated_data):
        university = University.objects.create(**validated_data)
        return university

class GymnasuimSerializers(serializers.ModelSerializer):
    image = serializers.ImageField()
    name = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=100)
    date_of_foundation = serializers.DateTimeField()
    filial = serializers.CharField(max_length=100)
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    Faculty =serializers.PrimaryKeyRelatedField(queryset=Faculty.objects.all())
    direction =serializers.PrimaryKeyRelatedField(queryset=Direction.objects.all())
    Dorm_room = serializers.PrimaryKeyRelatedField(queryset=Dorm_room.objects.all())

    class Meta:
        model=Gymnasium
        fields=('image','name','address','date_of_foundation','filial',
                'course','Faculty','direction','Door_room')

    def create(self, validated_data):
        gymnasium=Gymnasium.objects.create(**validated_data)
        return gymnasium



class ColledgeSerializers(serializers.ModelSerializer):
    image = serializers.ImageField()
    name = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=100)
    date_of_foundation = serializers.DateTimeField()
    filial = serializers.CharField(max_length=100)
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    Faculty =serializers.PrimaryKeyRelatedField(queryset=Faculty.objects.all())
    direction =serializers.PrimaryKeyRelatedField(queryset=Direction.objects.all())
    Dorm_room = serializers.PrimaryKeyRelatedField(queryset=Dorm_room.objects.all())

    class Meta:
        model = Colledge
        fields = ('image', 'name', 'address', 'date_of_foundation', 'filial',
                  'course', 'Faculty', 'direction', 'Door_room')

    def create(self, validated_data):
        college = Colledge.objects.create(**validated_data)
        return college


class AcademicSerializers(serializers.ModelSerializer):
    image = serializers.ImageField()
    name = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=100)
    date_of_foundation = serializers.DateTimeField()
    filial = serializers.CharField(max_length=100)
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    Faculty =serializers.PrimaryKeyRelatedField(queryset=Faculty.objects.all())
    direction =serializers.PrimaryKeyRelatedField(queryset=Direction.objects.all())
    Dorm_room = serializers.PrimaryKeyRelatedField(queryset=Dorm_room.objects.all())

    class Meta:
        model = Academic
        fields = ('image', 'name', 'address', 'date_of_foundation', 'filial',
                  'course', 'Faculty', 'direction', 'Door_room')

    def create(self, validated_data):
        academic = Academic.objects.create(**validated_data)
        return academic
