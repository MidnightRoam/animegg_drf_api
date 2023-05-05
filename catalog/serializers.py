from rest_framework.serializers import ModelSerializer

from .models import (
    Anime,
    Genre,
    AgeRestriction,
    Type,
    Status, AgeValue
)


class AnimeSerializer(ModelSerializer):
    """Anime object serializer"""
    class Meta:
        model = Anime
        fields = (
            'id',
            'title',
            'subtitle',
            'description',
            'release_date',
            'genres',
            'slug',
            'age_restrictions',
            'type',
            'status'
        )


class GenreSerializer(ModelSerializer):
    """Genre of anime serializer"""
    class Meta:
        model = Genre
        fields = ('id', 'title', 'description')


class AgeValueSerializer(ModelSerializer):
    """Age values of age restrictions serializer"""
    class Meta:
        model = AgeValue
        fields = ('id', 'value')


class AgeRestrictionSerializer(ModelSerializer):
    """Age restriction object serializer"""
    class Meta:
        model = AgeRestriction
        fields = ('id', 'age', 'description', 'abbreviation', 'title')


class TypeSerializer(ModelSerializer):
    """Type of anime serializer"""
    class Meta:
        model = Type
        fields = ('id', 'title', )


class StatusSerializer(ModelSerializer):
    """Status of anime serializer"""
    class Meta:
        model = Status
        fields = ('id', 'title', )
