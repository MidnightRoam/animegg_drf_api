from rest_framework.viewsets import ModelViewSet

from .models import Episode
from .serializers import EpisodeSerializer


class EpisodeModelViewSet(ModelViewSet):
    """Episode of anime model view set"""
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
