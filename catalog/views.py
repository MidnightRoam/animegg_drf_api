import random
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
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
    AnimeRatingSerializer,
    AnimeUserCommentSerializer,
    AnimeReviewSerializer,
    AnimeBookmarkListSerializer
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
    AnimeRating,
    AnimeUserComment,
    AnimeReview,
    AnimeBookmarkList
)


class AnimeViewSet(ModelViewSet):
    """Anime objects view set"""
    queryset = Anime.objects.all().prefetch_related('screenshot_set')
    serializer_class = AnimeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'type', 'genres', 'mpaa_rating']
    search_fields = ['title', 'subtitle', ]
    ordering_fields = ['release_date', 'created_at', 'title']

    def get_random_anime(self, request) -> Response:
        """Return random anime object"""
        random_anime = random.choice(self.queryset)
        serializer = AnimeSerializer(random_anime)
        return Response(serializer.data)

    def list(self, request):
        """Return a list of anime objects"""
        queryset = Anime.objects.prefetch_related(
            'screenshot_set',
            'related_anime',
            'main_characters',
            'genres'
        ).all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Return a selected anime object"""
        queryset = Anime.objects.get(pk=pk)
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.prefetch_related('related_anime')
        return queryset


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


class AnimeUserCommentViewSet(ModelViewSet):
    """Anime user comment model view set"""
    queryset = AnimeUserComment.objects.all()
    serializer_class = AnimeUserCommentSerializer

    def list(self, request):
        """Returns a list of all user comments"""
        queryset = self.queryset.prefetch_related('reply').all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class AnimeReviewViewSet(ModelViewSet):
    """Anime review model view set"""
    queryset = AnimeReview.objects.all()
    serializer_class = AnimeReviewSerializer


class AnimeBookmarkListViewSet(ModelViewSet):
    """User bookmark list of anime model view set"""
    queryset = AnimeBookmarkList.objects.all()
    serializer_class = AnimeBookmarkListSerializer

    def list(self, request):
        """Returns a list of all anime bookmark list objects"""
        queryset = self.queryset.prefetch_related('anime')
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
