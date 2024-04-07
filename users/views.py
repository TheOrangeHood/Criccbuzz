from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import UserCreateSerializer, UserLoginSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

# Create your views here.

class CreateAdminUserView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data = request.data)
        if serializer.is_valid(raise_exception=False):
            username = serializer.validated_data['username']
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = User.objects.create_user(
                username=username,
                password=password,
                email = email,
                is_staff=True
            )
            payload = {
                "status":'Admin Account successfully created',
                "status_code": 200,
                "user_id": user.id
            }
            return Response(payload)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginAdminUserView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data = request.data)
        if serializer.is_valid(raise_exception=False):
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            print(username, password)
            user = authenticate(username=username, password=password)

            if user is not None:
                tokens = self.get_tokens_for_user(user)
                payload = {
                    "status":'Login successful',
                    "status_code": 200,
                    "user_id": user.id,
                    "access_token":tokens["access"],
                    "refresh_token":tokens["refresh"]
                }
                return Response(payload)
            else:
                payload = {
                    "status":"Incorrect username/password provided. Please retry",
                    "status_code": 401
                }
                return Response(payload)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }