from rest_framework import serializers
from user.models import User
from student.models import\
    Student,\
    Course,\
    Faculty,\
    Direction,\
    Room,Dorm_room




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
    room_number = serializers.IntegerField(required=True)
    student_name = serializers.CharField(required=True)
    student_photo = serializers.ImageField(required=True)
    class Meta:
        model = Room
        fields=('room_number','student_name','student_photo',)


class Dorm_roomSerializers(serializers.ModelSerializer):

    number_room=RoomSerializers(required=True)

    address=serializers.CharField(required=True)
    dorm_building=serializers.IntegerField(required=True)
    # number_room=serializers.PrimaryKeyRelatedField(queryset=Room.objects)
    floor=serializers.IntegerField(required=True)

    class Meta:
        model=Dorm_room
        fields=('number_room','address','dorm_building','floor',)

class UserStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=('first_name','second_name','middle_name','age',
                'telephone_number','faculty','course',
                'direction','room')



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
            last_name=student_data['last_name'],
            age=student_data['age'],
            telephone_number=student_data['telephone_number'],
            faculty=student_data['faculty'],
            course=student_data['course'],
            direction=student_data['direction'],
            room=student_data['room']
        )

        return user





