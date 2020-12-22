from rest_framework import serializers
from user.models import User
from student.models import\
    student,PhoneNumber,\
    Course,\
    Faculty,\
    Direction,\
    Room


class PhoneNumberSerializers(serializers.ModelSerializer):

    class Meta:
        model=PhoneNumber


class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course


class FacultySerializers(serializers.ModelSerializer):
    class Meta:
        model = Faculty


class DirectionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Direction


class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room

class UserStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=student
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
        student.objects.create(
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





