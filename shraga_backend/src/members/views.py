from .serializers import *
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework import status 
from django.utils import timezone


@api_view(['POST'])
def register(request):
    try:
        new_user_serializer = RegisterSerializer(data=request.data)
        if not new_user_serializer.is_valid():
            print("(register-views) not valid: ", new_user_serializer.errors)
            return Response(new_user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        new_user = new_user_serializer.save()
        return Response({"message": "User created successfully", "user_id": new_user.id}, status=status.HTTP_201_CREATED)
    
    except Exception as err:
            print("Error during user creation: ", err)
            return Response({"error": "An error occurred while creating the user, please try again"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def login(request):
    try:
        user_login_serializer = LoginSerializer(data=request.data)
        if not user_login_serializer.is_valid():
            print("(login-views) not valid: ", user_login_serializer.errors)
            return Response(user_login_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        user = user_login_serializer.validated_data['user']
        user.last_login = timezone.localtime(timezone.now())
        user.save(update_fields=['last_login'])
        return Response({"message": "Login successful", "user_id": user.id}, status=status.HTTP_200_OK)
    
    except Exception as err:
        print("Error during user login: ", err)
        return Response({"error": "An error occurred while logging in, please try again"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)