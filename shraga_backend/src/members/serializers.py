from django.core.validators import MinLengthValidator, MaxLengthValidator, EmailValidator
from django.contrib.auth.models import User 
from rest_framework.serializers import ModelSerializer, Serializer, ValidationError, EmailField, CharField  
from django.utils import timezone
from django.contrib.auth import authenticate


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
        extra_kwargs = {
            'first_name': {'allow_blank': False, 'required':True, 'min_length': 2, 'max_length': 30,},
            'last_name': {'allow_blank': False, 'required':True, 'min_length': 2, 'max_length': 30,},
            'email': {'allow_blank': False, 'required':True, 'validators': [EmailValidator(message="Invalid email address"), MinLengthValidator(5), MaxLengthValidator(100)],},
            'password': {'write_only': True, 'min_length': 4, 'max_length': 150,}
            }

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise ValidationError("Email address already exists.")
        return value

    def create(self, validated_data):
        user = User(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            username=validated_data['email'],  # Use email as username
            last_login=timezone.localtime(timezone.now())
        )
        #create hash to password
        user.set_password(validated_data['password'])
        user.save()
        print("(RegisterSerializer) User created successfully: ", user)
        return user
    
    
class LoginSerializer(Serializer):
    email = EmailField(max_length=100, min_length=5, required = True, allow_blank = False)
    password = CharField(write_only=True, max_length=150, min_length=4, required = True, allow_blank = False)

    def validate(self, data):
        user = authenticate(username=data['email'], password=data['password'])
        if user is None:
            raise ValidationError({"non_field_errors": ["Invalid credentials"]})
        data['user'] = user
        print("(LoginSerializer) User login successfully: ", user)
        return data