from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .serializers import MyInfoUserSerializer
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ParseError

# Create your views here.

class Users(APIView):
    #read
    # def get(self, request):
    #     user = request.user
    #     serializer = MyInfoUserSerializer(request.data)
    #     return Response(serializer.data)
    
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