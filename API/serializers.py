from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product

class ProfileSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type' : 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')
        extra_kwargs = {
            'password' : {'write_only' : True}
        }

    def save(self):
        user = User(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password' : 'passwords do not match'})
        user.set_password(password)
        user.save()
        return user

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('product_name','product_category','product_price','thumbnail')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email')