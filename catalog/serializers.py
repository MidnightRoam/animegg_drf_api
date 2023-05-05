from rest_framework.serializers import ModelSerializer

from .models import Anime, Genre


class AnimeSerializer(ModelSerializer):
    """Anime object serializer"""
    class Meta:
        model = Anime
        fields = ('id', 'title', 'subtitle', 'description', 'release_date', 'genres', 'slug')


class GenreSerializer(ModelSerializer):
    """Genre of anime serializer"""
    class Meta:
        model = Genre
        fields = ('id', 'title', 'description')


# class AgeRestrictions
