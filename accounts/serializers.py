from rest_framework import serializers
from .models import User, Profile, Doctor

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'role', 'phone_number')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        if user.role == 'PATIENT':
            Profile.objects.create(user=user)
        return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
