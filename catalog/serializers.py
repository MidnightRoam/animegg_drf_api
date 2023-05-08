from rest_framework.serializers import ModelSerializer

from .models import (
    Anime,
    Genre,
    AgeRestriction,
    Type,
    Status,
    AgeValue,
    MPAARating,
    Origin
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
            'poster',
            'main_characters',
            'release_date',
            'genres',
            'origin',
            'slug',
            'age_restrictions',
            'type',
            'status',
        )


class GenreSerializer(ModelSerializer):
    """Genre of anime serializer"""
    class Meta:
        model = Genre
        fields = ('id', 'title', 'description', 'slug',)


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


class MPAARatingSerializer(ModelSerializer):
    """MPAARating serializer"""
    class Meta:
        model = MPAARating
        fields = ('id', 'title', 'abbreviation', 'description')


class TypeSerializer(ModelSerializer):
    """Type of anime serializer"""
    class Meta:
        model = Type
        fields = ('id', 'title', 'slug',)


class StatusSerializer(ModelSerializer):
    """Status of anime serializer"""
    class Meta:
        model = Status
        fields = ('id', 'title', 'slug',)


class OriginSerializer(ModelSerializer):
    """Origin of anime serializer"""
    class Meta:
        model = Origin
        fields = ('id', 'title', 'slug', )
