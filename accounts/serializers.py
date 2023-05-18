from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

UserModel = get_user_model()


class UserSerializer(ModelSerializer):
    """User object serializer"""
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = ('id', 'username', 'email', 'slug', 'password', 'password2', 'friends')

    def create(self, validated_data):
        password = validated_data['password']
        password2 = validated_data['password2']
        email = validated_data['email']
        username = validated_data['username']

        if password != password2:
            raise serializers.ValidationError({"Error": "Passwords does not match"})

        if len(password) < 8:
            raise serializers.ValidationError({"Error": "Password must be at least 8 characters"})

        if UserModel.objects.filter(email=email).exists():
            raise serializers.ValidationError({"Error": "User with that email already exists"})

        user = UserModel.objects.create(
            username=username,
            email=email,
            password=make_password(password),
        )

        return user

