from rest_framework.serializers import ModelSerializer

from .models import Manga


class MangaSerializer(ModelSerializer):
    """Manga object serializer"""
    class Meta:
        model = Manga
        fields = ('id', 'title', 'subtitle', 'volumes', 'chapters', 'type', 'slug', )