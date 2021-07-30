from django.contrib.auth import authenticate
from django.http import response
from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from .serializers import ProfileSerializer, ListSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Products

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

@permission_classes((permissions.AllowAny,))
class TokenView(APIView):
    def post(self, request,):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token = Token.objects.get_or_create(user=User)
            return Response({"token" : user.auth_token.key})
        else:
            return Response({"error" : "Wrong credentials"}, status = status.HTTP_400_BAD_REQUEST)

    def get(self,):
        for user in User.objects.all():
            token = Token.objects.get(user=user)
            if token:
                return Response({user.username : user.auth_token.key})
            else:
                return Response({"error" : "Wrong credentials"}, status = status.HTTP_400_BAD_REQUEST)

class productList(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = ListSerializer

    def get_queryset(self):
        return Products.objects.all()