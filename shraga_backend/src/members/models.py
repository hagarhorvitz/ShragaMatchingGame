# from django.core.validators import MinLengthValidator, MaxLengthValidator, EmailValidator
# from django.contrib.auth.models import User 
# from rest_framework.serializers import ModelSerializer, Serializer, ValidationError, EmailField, CharField  
# from django.utils import timezone
# from django.contrib.auth import authenticate


# class RegistrationForm(ModelForm):
#     class Meta:
#         model = User 
#         fields = ["first_name", "last_name", "email", "password"]
       
#         widgets = {
#             "first_name": TextInput(attrs = { "class": "form-control", "minlength": 2, "maxlength": 30 }), # attrs = HTML Attributes
#             "last_name": TextInput(attrs = { "class": "form-control", "minlength": 2, "maxlength": 30 }), # attrs = HTML Attributes
#             "email": EmailInput(attrs = { "class": "form-control", "minlength": 5, "maxlength": 100 }),
#             "password": PasswordInput(attrs = { "class": "form-control", "minlength": 5, "maxlength": 20 }),
#         }

#     def save(self):

#         #create user without saving to db 
#         user = super().save(commit=False)

#         #save username as email 
#         user.username = self.cleaned_data["email"]

#         #create hash to password
#         user.password = make_password(self.cleaned_data["password"])

#         user.save() 
#         return user 


# class LoginForm(ModelForm):
#     class Meta:
#         model = User 
#         fields = ["email", "password"]
#         widgets = {
#             "email": EmailInput(attrs = { "class": "form-control", "minlength": 5, "maxlength": 100 }),
#             "password": PasswordInput(attrs = { "class": "form-control", "minlength": 5, "maxlength": 20 }),
#         }





# class MembersModel(Model):

#     first_name = CharField(max_length = 20, validators = [MinLengthValidator(2), MaxLengthValidator(50)])
#     last_name = CharField(max_length = 30, validators = [MinLengthValidator(2), MaxLengthValidator(50)])
#     email = EmailField(max_length = 80, validators = [EmailValidator("Enter valid email address"), MinLengthValidator(5), MaxLengthValidator(100)])
#     password = CharField(max_length = 275, validators = [MinLengthValidator(5), MaxLengthValidator(300)])

#     class Meta:
#         db_table = "members"
