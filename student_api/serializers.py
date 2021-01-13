from rest_framework import serializers
from user.models import User
from student.models import \
    Student, \
    Course, \
    Faculty, \
    Direction, \
    Room, Dorm_room, Dorm_building, Floor


class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields=('kurs_number',)




class FacultySerializers(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields=('faculty_number',)


class DirectionSerializers(serializers.ModelSerializer):
    direction_name=serializers.CharField(required=True)

    class Meta:
        model=Direction
        fields=('direction_name',)


class RoomSerializers(serializers.ModelSerializer):
    # room_number = serializers.IntegerField(required=True)
    # student_name = serializers.CharField(required=True)
    # student_photo = serializers.ImageField(required=True)
    class Meta:
        model = Room
        fields=('room_number','student_name','student_photo',)



class Dorm_buildingSerializers(serializers.ModelSerializer):

    def create(self, validated_data):
        return Dorm_building.objects.all()

    class Meta:
        model=Dorm_building
        fields=('number_building','dorm_room')



class FLoorSerializers(serializers.ModelSerializer):
    dorm_building=serializers.PrimaryKeyRelatedField(queryset=Floor.objects.all())

    def create(self, validated_data):
        return Floor.objects.all()

    class Meta:
        model=Floor
        fields=('number_floor','dorm_building')





class Dorm_roomSerializers(serializers.ModelSerializer):



    class Meta:
        model=Dorm_room
        fields=('title','address')




class UserStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=('first_name','second_name','middle_name','age',
                'telephone_number','faculty','course',
                'direction','dorm_room')



class StudentRegisterSerializer(serializers.ModelSerializer):
    student=UserStudentSerializer(required=True)
    class Meta:
        model=User
        fields=('email','password','student')
        extra_kwargs={
            'password':{'write_only':True}
        }

    def create(self, validated_data):
        student_data=validated_data.pop('student')
        user=User.objects.create_user(**validated_data)
        Student.objects.create(
            user=user,
            first_name=student_data['first_name'],
            second_name=student_data['second_name'],
            age=student_data['age'],
            telephone_number=student_data['telephone_number'],
            faculty=student_data['faculty'],
            course=student_data['course'],
            direction=student_data['direction'],
            dorm_room=student_data['dorm_room']
        )

        return user





