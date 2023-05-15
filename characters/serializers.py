from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import (
    Character
)
# from catalog.serializers import AnimeSerializer


class CharacterSerializer(ModelSerializer):
    """Character serializer"""
    # anime = serializers.SerializerMethodField()

    class Meta:
        model = Character
        fields = (
            'id',
            'name',
            'subname',
            'image',
            'description',
            'anime',
            'slug',
        )


    # def get_anime(self, obj):
    #     anime = obj.anime.all()
    #     serializer = AnimeSerializer(anime, many=True)
    #     return serializer.data
