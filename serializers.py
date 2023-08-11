from rest_framework import serializers
from .models import CustomUser

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})


    def validate_gender(self, value):
        valid_genders = [choice[0] for choice in CustomUser.GENDER_CHOICES]
        if value not in valid_genders:
            raise serializers.ValidationError("Invalid gender value.")
        return value


    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'age', 'gender')
        extra_kwargs = {'username': {'required': False}}


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
