from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from django.contrib import auth
from django.contrib.auth import authenticate, login


def index(request):
	return render(request, 'login.html')


def register(request):
	return render(request, 'register.html')


""" Creates the User """
class UserCreate(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            if user:
                login(request,user)
                return HttpResponseRedirect('/products/')

        else:
            # return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
            return render(request, 'register.html', {'error_message': serializer.errors})


""" login the User """
class Login(APIView):
    permission_classes = (AllowAny,)

    @csrf_exempt
    def post(self,request, *args, **kwargs):
        username = request.data.get("email")
        password = request.data.get("password")

        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'},
                            status=HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/products/')
        else:
        	return render(request, 'login.html', {'error_message': 'Incorrect username and / or password.'})


""" Logout Request """
def logout_user(request):
    auth.logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)

