from rest_framework.viewsets import ModelViewSet

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
