from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from .serializers import UserSerializer


class UserModelViewSet(ModelViewSet):
    """User object model view set"""
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
