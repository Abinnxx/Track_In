from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Profile
from .serializers import AdditionalDetailsSerializers,LicenseDetailsSerializers

import random
import string

def generate_random_password(length=12):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits

    all_characters = lowercase_letters + uppercase_letters + digits 
    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
    ]

    password += random.choices(all_characters, k=length - 4)
    random.shuffle(password)
    print(''.join(password))
    return ''.join(password)


class AdminAddUsersApi(APIView):
    def post(self,request):
        data=request.data
        password=generate_random_password(9)
        email=data.get('email')
        first_name=data.get('firstname')
        last_name=data.get('lastname')
        role=data.get("role")
        try:
            user = Profile.objects.create_user(first_name=first_name,last_name=last_name,password=password,email=email,role=role,username=email,password_str=password)
            return Response({"msg": "user added successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"msg": "something went wrong","error":str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class RegistrationUserApi(APIView):
    def post(self,request):
        data=request.data.copy()
        first_name=data.get('firstname')
        last_name=data.get('lastname')
        role='internal_user'
        password=data.get('password')
        email=data.get('email')

        try:
            user=Profile.objects.create_user(first_name=first_name,last_name=last_name,role=role,password=password,username=email,email=email)
            data['profile']=user.id
            data['password_str']=password  
            print(data)
            
            details_serializer=AdditionalDetailsSerializers(data=data)
            if details_serializer.is_valid():
                details_serializer.save()
                return Response({'msg':'Registration succesfull'},status=status.HTTP_201_CREATED)
            else:
                user.delete()
                return Response(details_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
        except:
            return Response({'msg':'registration failed'},status=status.HTTP_400_BAD_REQUEST)


class AddLicense(APIView):
    def post(self,request):
        fromdata=request.data
        serializer=LicenseDetailsSerializers(data=fromdata)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"license added successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"msg":"failed to add"},status=status.HTTP_400_BAD_REQUEST)