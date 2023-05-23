from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
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

    def list(self, request):
        """Returns a list of all character objects"""
        queryset = self.queryset.prefetch_related('anime').all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
