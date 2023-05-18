from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from .models import (
    Character
)

from .serializers import (
    CharacterSerializer
)


class CharacterModelViewSet(ModelViewSet):
    """Character model view set"""
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['anime', ]
    search_fields = ['name', 'subname']
