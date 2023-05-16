import random
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response


from .serializers import (
    AnimeSerializer,
    GenreSerializer,
    AgeValueSerializer,
    AgeRestrictionSerializer,
    TypeSerializer,
    StatusSerializer,
    MPAARatingSerializer,
    OriginSerializer,
    ScreenshotSerializer,
    AnimeRatingSerializer
)
from .models import (
    Anime,
    Genre,
    AgeValue,
    AgeRestriction,
    Type,
    Status,
    MPAARating,
    Origin,
    Screenshot,
    AnimeRating
)


class AnimeViewSet(ModelViewSet):
    """Anime objects view set"""
    queryset = Anime.objects.all().prefetch_related('screenshot_set')
    serializer_class = AnimeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_random_anime(self, request):
        """Return random anime object"""
        random_anime = random.choice(self.queryset)
        serializer = AnimeSerializer(random_anime)
        return Response(serializer.data)


class GenreViewSet(ModelViewSet):
    """Genre of anime view set"""
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class AgeValueViewSet(ModelViewSet):
    """Age value for age restriction view set"""
    queryset = AgeValue.objects.all()
    serializer_class = AgeValueSerializer


class AgeRestrictionViewSet(ModelViewSet):
    """Age restriction view set"""
    queryset = AgeRestriction.objects.all()
    serializer_class = AgeRestrictionSerializer


class MPAARatingModelViewSet(ModelViewSet):
    """MPAARating model view set"""
    queryset = MPAARating.objects.all()
    serializer_class = MPAARatingSerializer


class TypeViewSet(ModelViewSet):
    """Type of anime view set"""
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class StatusViewSet(ModelViewSet):
    """Status of anime model view set"""
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class OriginModelViewSet(ModelViewSet):
    """Origin of anime model view set"""
    queryset = Origin.objects.all()
    serializer_class = OriginSerializer


class ScreenshotViewSet(ModelViewSet):
    """Anime screenshot model view set"""
    queryset = Screenshot.objects.all()
    serializer_class = ScreenshotSerializer


class AnimeRatingViewSet(ModelViewSet):
    """Anime rating model view set"""
    queryset = AnimeRating.objects.all()
    serializer_class = AnimeRatingSerializer
