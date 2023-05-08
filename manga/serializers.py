from rest_framework.serializers import ModelSerializer

from .models import (
    Manga,
    Type,
    Status,
    Genre
)


class MangaSerializer(ModelSerializer):
    """Manga object serializer"""
    class Meta:
        model = Manga
        fields = (
            'id',
            'title',
            'subtitle',
            'volumes',
            'chapters',
            'characters',
            'released',
            'finished',
            'type',
            'slug',
        )


class TypeSerializer(ModelSerializer):
    """Manga type object serializer"""
    class Meta:
        model = Type
        fields = ('id', 'title', 'slug', )


class StatusSerializer(ModelSerializer):
    """Status object serializer"""
    class Meta:
        model = Status
        fields = ('id', 'title', 'slug', )


class GenreSerializer(ModelSerializer):
    """Genre object serializer"""
    class Meta:
        model = Genre
        fields = ('id', 'title', 'description', 'slug', )
