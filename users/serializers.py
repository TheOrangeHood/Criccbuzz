from rest_framework import serializers
from django.contrib.auth.models import User

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
    
    def validate(self, attrs):
        if attrs.get('email') is None:
            raise serializers.ValidationError("Email cannot be empty")
        return super().validate(attrs)

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()