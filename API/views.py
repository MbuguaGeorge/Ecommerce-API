from django.contrib.auth import authenticate
from rest_framework import generics, permissions, status
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from .serializers import ProfileSerializer, ListSerializer, UserSerializer, CartSerializer, SaveSerializer, NewSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Product, Cart, Favourite, New_Arrival
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

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
        serializer = UserSerializer(user)
        if user:
            token = Token.objects.get_or_create(user=user)
            return Response({"token" : user.auth_token.key,"user":serializer.data})
        else:
            return Response({"error" : "Wrong credentials"}, status = status.HTTP_400_BAD_REQUEST)

class CurView(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self, request,):
        for user in User.objects.all():
            if request.user.is_authenticated:
                serializer = UserSerializer(request.user)
                return Response({"user":serializer.data})
            else:
                return Response({"error":"not authenticated"})

class productList(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = ListSerializer

    def get_queryset(self):
        return Product.objects.all()

class userList(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return User.objects.all()

@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def add(request, pk):
    product = get_object_or_404(Product, id=pk)
    if request.user.is_authenticated:
        mycart, _ = Cart.objects.get_or_create(user=request.user)
        mycart.product.add(product)
        return Response({'item added'})
    else:
        return Response({'error'})


@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def remove(request, pk):
    product = get_object_or_404(Product, id=pk)
    if request.user.is_authenticated:
        mycart, _ = Cart.objects.get_or_create(user=request.user)
        mycart.product.remove(product)
        return Response({'item removed'})
    else:
        return Response({'error'})

class CartView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self,request):
        cart = Cart.objects.get(user=request.user)
        serializer = CartSerializer(cart)
        return Response({"cart" : serializer.data})

@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def favourite(request,pk):
    product = get_object_or_404(Product, id=pk)
    if request.user.is_authenticated:
        saved, _ = Favourite.objects.get_or_create(user=request.user)
        saved.product.add(product)
        return Response({'product saved as favourite'})
    else:
        return Response({'error'})
    
class SaveView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        favourite = Favourite.objects.get(user=request.user)
        serializer = SaveSerializer(favourite)
        return Response({"favourite" : serializer.data})

class NewList(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = NewSerializer

    def get_queryset(self):
        return New_Arrival.objects.all()