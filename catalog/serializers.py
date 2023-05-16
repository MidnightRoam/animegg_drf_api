from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import (
    Anime,
    Genre,
    AgeRestriction,
    Type,
    Status,
    AgeValue,
    MPAARating,
    Origin,
    Screenshot,
    AnimeRating
)
from characters.serializers import CharacterSerializer


class ScreenshotSerializer(ModelSerializer):
    """Anime screenshot serializer"""
    class Meta:
        model = Screenshot
        fields = ('id', 'anime', 'image')


class AnimeSerializer(ModelSerializer):
    """Anime object serializer"""
    main_characters = serializers.SerializerMethodField()
    genres = serializers.SerializerMethodField()
    age_restrictions = serializers.SerializerMethodField()
    screenshot_set = ScreenshotSerializer(many=True, required=False)

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
            'screenshot_set',
        )

    def get_main_characters(self, obj):
        """ORM query optimization for main characters field"""
        main_characters = obj.main_characters.all()
        serializer = CharacterSerializer(main_characters, many=True)
        return serializer.data

    def get_genres(self, obj):
        """ORM query optimization for genres field"""
        genres = obj.genres.all()
        serializer = GenreSerializer(genres, many=True)
        return serializer.data

    def get_age_restrictions(self, obj):
        """ORM query optimization for age restrictions field"""
        age_restrictions = obj.age_restrictions
        serializer = AgeRestrictionSerializer(age_restrictions, many=False)
        return serializer.data

    def get_screenshot_set(self, obj):
        """ORM query optimization for anime screenshots"""
        screenshot_set = obj.screenshots
        serializer = ScreenshotSerializer(screenshot_set, many=True)
        return serializer.data


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


class AnimeRatingSerializer(ModelSerializer):
    """Anime rating serializer"""
    class Meta:
        model = AnimeRating
        fields = ('id', 'user', 'anime', 'value')
