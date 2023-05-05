from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import (
    AnimeSerializer,
    GenreSerializer
)
from .models import (
    Anime,
    Genre
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