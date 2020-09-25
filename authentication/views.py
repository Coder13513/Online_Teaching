from django.shortcuts import render
from .serializer import RegisterSerializer,LoginSerializer
from rest_framework import generics,mixins,status
from rest_framework.response import Response
from .models import User
from django.contrib.auth import authenticate,login
from rest_framework_jwt.settings import api_settings
from utils.permissions import NonRegisteredUserOnly,SuperUserOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework.authtoken.models import Token


class LoginWithTokenAuthenticationAPIView(generics.GenericAPIView):
    serializer_class    =      LoginSerializer
    permission_classes     =   [NonRegisteredUserOnly]
    authentication_classes =   []

    def post(self,request):
        print(request.data)
        username    =   request.data.get('username')
        password    =   request.data.get('password')
        print(username)
        print(password)
        user        =   authenticate(username=username,password=password)
        print(user)
        print(user.role)
        x="ADMIN"
        print(x)
        if user is not None :
            if  user.role == x:    
                token, _= Token.objects.get_or_create(user = user)          
                return Response({
                        "data":
                                    {
                                        "message":"successfully logged in ",
                                        'token': token.key,
                                        'role':user.role
                                        }
                                        },
                                        status=status.HTTP_200_OK)   
            response = {
        "data": {
            "message": "Your login information is invalid",
            "status": "invalid"
        }
    }
        return Response(response, status=status.HTTP_200_OK)



    


class LoginWithTokenAuthenticationAPIViewS(generics.GenericAPIView):
    serializer_class    =       LoginSerializer
    permission_classes     =   [NonRegisteredUserOnly]
    authentication_classes =   []

    def post(self,request):
        print(request.data)
        username    =   request.data.get('username')
        password    =   request.data.get('password')
        print(username)
        print(password)
        user        =   authenticate(username=username,password=password)
        print(user)
        print(user.role)
        x="STUDENT"
        print(x)
        if user is not None :
            # r=user.role
            # print(r)
            # y = 'STUDENT'
            if  user.role == x:      
                token, _= Token.objects.get_or_create(user = user)          
                return Response({
                        "data":
                                    {
                                        "message":"successfully logged in ",
                                        'token': token.key,
                                        'role':user.role
                                        }
                                        },
                                        status=status.HTTP_200_OK)   
            response = {
        "data": {
            "message": "Your login information is invalid",
            "status": "invalid"
        }
    }
        return Response(response, status=status.HTTP_200_OK)



class LoginWithTokenAuthenticationAPIViewT(generics.GenericAPIView):
    serializer_class    =       LoginSerializer
    permission_classes     =   [NonRegisteredUserOnly]
    authentication_classes =   []

    def post(self,request):
        print(request.data)
        username    =   request.data.get('username')
        password    =   request.data.get('password')
        print(username)
        print(password)
        user        =   authenticate(username=username,password=password)
        print(user)
        print(user.role)
        x="TEACHER"
        print(x)
        if user is not None :
            # r=user.role
            # print(r)
            # y = 'STUDENT'
            if  user.role == x:      
                token, _= Token.objects.get_or_create(user = user)          
                return Response({
                        "data":
                                    {
                                        "message":"successfully logged in ",
                                        'token': token.key,
                                        'role':user.role
                                        }
                                        },
                                        status=status.HTTP_200_OK)   
            response = {
        "data": {
            "message": "Your login information is invalid",
            "status": "invalid"
        }
    }
        return Response(response, status=status.HTTP_200_OK)



    

    





# #TOKEN STUFF
#     token, _ = Token.objects.get_or_create(user = user)
    
#     #token_expire_handler will check, if the token is expired it will generate new one
#     is_expired, token = token_expire_handler(token)     # The implementation will be described further
#     user_serialized = UserSerializer(user)

#     return Response({
#         'user': user_serialized.data, 
#         'expires_in': expires_in(token),
#         'token': token.key
#     }, status=HTTP_200_OK)


class RegisterAPIView(generics.CreateAPIView):
     queryset               =   User.objects.all()
     permission_classes     =   [NonRegisteredUserOnly]
     authentication_classes =   []
     serializer_class       =   RegisterSerializer

     def post(self,request,*args,**kwargs):
        try:
            return self.create(request,*args,**kwargs)
        except:
            return Response({"message":"provided details is invalid"})
