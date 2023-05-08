from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Manga
from .serializers import MangaSerializer


class MangaModelViewSet(ModelViewSet):
    """Manga model view set"""
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer
