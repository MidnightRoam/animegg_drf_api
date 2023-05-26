from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import (
    Manga,
    Type,
    Status,
    Genre
)
from characters.serializers import CharacterSerializer


class MangaSerializer(ModelSerializer):
    """Manga object serializer"""
    characters = serializers.SerializerMethodField()
    genres = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()

    class Meta:
        model = Manga
        fields = (
            'id',
            'title',
            'subtitle',
            'volumes',
            'chapters',
            'genres',
            'characters',
            'released',
            'finished',
            'type',
            'slug',
        )

    def get_characters(self, obj):
        """ORM query optimization for characters field"""
        characters = obj.characters.all()
        serializer = CharacterSerializer(characters, many=True)
        return serializer.data

    def get_genres(self, obj):
        """ORM query optimization for genres field"""
        genres = obj.genres.all()
        serializer = GenreSerializer(genres, many=True)
        return serializer.data

    def get_type(self, obj):
        """ORM query optimization for type field"""
        type = obj.type
        serializer = TypeSerializer(type, many=False)
        return serializer.data


class TypeSerializer(ModelSerializer):
    """Manga type object serializer"""
    class Meta:
        model = Type
        fields = ('id', 'title', 'slug', )
        ref_name = 'manga_type'


class StatusSerializer(ModelSerializer):
    """Status object serializer"""
    class Meta:
        model = Status
        fields = ('id', 'title', 'slug', )
        ref_name = 'manga_status'


class GenreSerializer(ModelSerializer):
    """Genre object serializer"""
    class Meta:
        model = Genre
        fields = ('id', 'title', 'description', 'slug', )
        ref_name = 'manga_genre'
