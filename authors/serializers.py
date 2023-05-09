from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from manga.serializers import MangaSerializer
from .models import Author, Responsibility
from manga.serializers import MangaSerializer


class AuthorSerializer(ModelSerializer):
    """Author serializer class"""
    responsibilities = serializers.SerializerMethodField()

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

    def get_responsibilities(self, obj):
        """ORM query optimization for responsibilities field"""
        responsibilities = obj.responsibilities.all()
        serializer = ResponsibilitySerializer(responsibilities, many=True)
        return serializer.data


class ResponsibilitySerializer(ModelSerializer):
    """Responsibility serializer class"""
    class Meta:
        model = Responsibility
        fields = (
            'id',
            'title',
        )
