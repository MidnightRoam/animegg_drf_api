from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from manga.serializers import MangaSerializer
from .models import Author


class AuthorSerializer(ModelSerializer):
    """Author serializer class"""

    class Meta:
        model = Author
        fields = (
            'id',
            'first_name',
            'last_name',
            'subname',
            'slug',
            'responsibilities',
            'image',
            'manga',
            'anime',
        )
