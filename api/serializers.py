from .models import Student
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'id',
            'f_name',
            'l_name',
            'email',
            'phone_no',
            'dob',
            'password',
            'cnic',
            'role',
            'gender',
            'image',
        ]

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
