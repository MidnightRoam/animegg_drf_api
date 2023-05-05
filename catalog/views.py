from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import (
    AnimeSerializer,
    GenreSerializer,
    AgeValueSerializer,
    AgeRestrictionSerializer,
    TypeSerializer,
    StatusSerializer,

)
from .models import (
    Anime,
    Genre,
    AgeValue,
    AgeRestriction,
    Type,
    Status,
)


class AnimeViewSet(ModelViewSet):
    """Anime objects viewset"""
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class GenreViewSet(ModelViewSet):
    """Genre of anime viewset"""
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class AgeValueViewSet(ModelViewSet):
    """Age value for age restriction viewset"""
    queryset = AgeValue.objects.all()
    serializer_class = AgeValueSerializer


class AgeRestrictionViewSet(ModelViewSet):
    """Age restriction viewset"""
    queryset = AgeRestriction.objects.all()
    serializer_class = AgeRestrictionSerializer


class TypeViewSet(ModelViewSet):
    """Type of anime viewset"""
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class StatusViewSet(ModelViewSet):
    """Status of anime viewset"""
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

