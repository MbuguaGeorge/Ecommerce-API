from django.http import response
from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import ProfileSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

# Create your views here.
@api_view(['POST',])
@permission_classes((permissions.AllowAny,))
def register(request):
    if request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "success"
            data['email'] = user.email
            data['username'] = user.username
        else:
            data = serializer.errors
        return Response(data)