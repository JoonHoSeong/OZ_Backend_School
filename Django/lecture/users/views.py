from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .serializers import MyInfoUserSerializer
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ParseError
from rest_framework.authentication import TokenAuthentication #사용자 인증
from rest_framework.permissions import IsAuthenticated #권한 
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
import jwt
from django.conf import settings
from config.authentication import JWTAuthentication

# Create your views here.

class Users(APIView):
    
    def post(self, request):
        password = request.data.get('password')
        serializer = MyInfoUserSerializer(data = request.data)
        try :
            validate_password(password)
        except :
            raise Response(serializer.errors)
        
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()
            
            serializer = MyInfoUserSerializer(user)
            return Response(serializer.data)
        else :
            raise Response(serializer.errors)
        
class MyInfo(APIView):
    authentication_classes = [TokenAuthentication] 
    permission_classes = [IsAuthenticated] 
    
    def get(self, request) :
        user = request.user
        serializer = MyInfoUserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request) :
        user = request.user
        serializer = MyInfoUserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            raise Response(serializer.errors)

#api/v1/users/login 
class Login(APIView) :
    def post(self, request) :
        username = request.data.get('username')
        password = request.data.get('password')
        
        if not username or not password :
            raise ParseError()
        
        user = authenticate(request=request, username=username, password=password)
        
        if user :
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        else :
            return Response(status=status.HTTP_400_BAD_REQUEST)
            
#api/v1/users/logout
class Logout(APIView) :
    permission_classes = [IsAuthenticated]
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
    
    
class JWTLogin(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        if not username or not password :
            raise ParseError()
        
        user = authenticate(request=request, username=username, password=password)
        
        if user :
            payload = {"id" : user.id, "username" : user.username}
            token = jwt.encode(
                payload=payload, key = settings.SECRET_KEY, algorithm="HS256"
            )
            
            return Response({"token" : token})
        
        
class UserDetailView(APIView):
    # authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({"id" : user.id, "username" : user.username})