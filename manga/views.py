from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .models import (
    Manga,
    Type,
    Status,
    Genre
)
from .serializers import (
    MangaSerializer,
    TypeSerializer,
    StatusSerializer,
    GenreSerializer
)


class MangaModelViewSet(ModelViewSet):
    """Manga model view set"""
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['genres', 'type', ]
    search_fields = ['title', 'subtitle', ]
    ordering_fields = ['created_at', 'released', 'title']


class TypeModelViewSet(ModelViewSet):
    """Type model view set"""
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class StatusModelViewSet(ModelViewSet):
    """Status model view set"""
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class GenreModelViewSet(ModelViewSet):
    """Genre model view set"""
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
