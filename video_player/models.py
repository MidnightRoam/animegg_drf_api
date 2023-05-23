from django.db import models

from catalog.models import Anime


class Episode(models.Model):
    """Anime episode for video player"""
    title = models.CharField(max_length=255)
    release_date = models.DateField(blank=True, null=True)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, default=None)
    video_url = models.URLField()
    episode_number = models.PositiveIntegerField()

