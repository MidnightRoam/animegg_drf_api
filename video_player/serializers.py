from rest_framework.serializers import ModelSerializer

from .models import Episode


class EpisodeSerializer(ModelSerializer):
    """Anime episode serializer"""
    class Meta:
        model = Episode
        fields = ('id', 'title', 'anime', 'episode_number', 'video_url')

