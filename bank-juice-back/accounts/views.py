from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth import get_user_model

from .serializers import UserSerializer

# Create your views here.

@api_view(['POST',])
def profile_update(request):
    if request.method == 'POST':
        user_profile = get_user_model().objects.get(username=request.user.username)
        
        serializer = UserSerializer(user_profile, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(serializer.data)


@api_view(['GET',])
def user_info(request):
    if request.method == 'GET':
        user = get_user_model().objects.get(username=request.user.username)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    

@api_view(['GET',])
def user_staff(request):
    if request.method == 'GET':
        user = get_user_model().objects.get(username=request.user.username)
        
        return Response({f'{user.is_staff}'})