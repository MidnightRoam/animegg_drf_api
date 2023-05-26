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
    AnimeBookmarkListSerializer,
    CommentLikeSerializer,
    CommentDislikeSerializer,
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
    AnimeBookmarkList,
    CommentLike,
    CommentDislike,
)

from catalog.permissions import IsStaffOrReadOnly


class AnimeViewSet(ModelViewSet):
    """
    View set for managing anime objects.

    Attributes:
        queryset (QuerySet): The queryset of all anime objects.
        serializer_class (Serializer): The serializer class used for serializing/deserializing anime data.
        permission_classes (tuple): The permission classes applied to the view set.
        filter_backends (list): The list of filter backends used for filtering the queryset.
        filterset_fields (list): The list of fields available for filtering the queryset.
        search_fields (list): The list of fields available for searching the queryset.
        ordering_fields (list): The list of fields available for ordering the queryset.
    """
    queryset = Anime.objects.all().prefetch_related('screenshot_set')
    serializer_class = AnimeSerializer
    permission_classes = (IsStaffOrReadOnly, )
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'type', 'genres', 'mpaa_rating']
    search_fields = ['title', 'subtitle', ]
    ordering_fields = ['release_date', 'created_at', 'title']

    def get_random_anime(self, request) -> Response:
        """
        Return random anime object.

        Returns:
            Response: The serialized data of the random anime object.
        """
        random_anime = random.choice(self.queryset)
        serializer = AnimeSerializer(random_anime)
        return Response(serializer.data)

    def list(self, request):
        """
        Return a list of anime objects.

        Returns:
            Response: The serialized data of the list of anime objects.
        """
        queryset = Anime.objects.prefetch_related(
            'screenshot_set',
            'related_anime',
            'main_characters',
            'genres'
        ).all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Return a selected anime object.

        Args:
            pk (int): The primary key of the anime object.

        Returns:
            Response: The serialized data of the selected anime object.
        """
        queryset = Anime.objects.get(pk=pk)
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)

    def get_queryset(self):
        """
        Get a queryset of anime objects.

        Returns:
            QuerySet: The filtered queryset of anime objects.
        """
        queryset = super().get_queryset()
        queryset = queryset.prefetch_related('related_anime')
        return queryset


class GenreViewSet(ModelViewSet):
    """
    View set for managing anime genre objects.

    Attributes:
        queryset (QuerySet): The queryset of all genres.
        serializer_class (Serializer): The serializer class used for serializing/deserializing genres data.
        permission_classes (tuple): The permission classes applied to the view set.
    """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsStaffOrReadOnly, )


class AgeValueViewSet(ModelViewSet):
    """
    View set for managing age value objects.

    Attributes:
        queryset (QuerySet): The queryset of all age value objects.
        serializer_class (Serializer): The serializer class used for serializing/deserializing age value data.
        permission_classes (tuple): The permission classes applied to the view set.
    """
    queryset = AgeValue.objects.all()
    serializer_class = AgeValueSerializer
    permission_classes = (IsStaffOrReadOnly, )


class AgeRestrictionViewSet(ModelViewSet):
    """
    View set for managing age restriction objects.

    Attributes:
        queryset (QuerySet): The queryset of all age restriction objects.
        serializer_class (Serializer): The serializer class used for serializing/deserializing age restriction data.
        permission_classes (tuple): The permission classes applied to the view set.
    """
    queryset = AgeRestriction.objects.all()
    serializer_class = AgeRestrictionSerializer
    permission_classes = (IsStaffOrReadOnly, )


class MPAARatingModelViewSet(ModelViewSet):
    """
    View set for managing MPAARating objects.

    Attributes:
        queryset (QuerySet): The queryset of all MPAA rating objects.
        serializer_class (Serializer): The serializer class used for serializing/deserializing MPAA rating data.
        permission_classes (tuple): The permission classes applied to the view set.
    """
    queryset = MPAARating.objects.all()
    serializer_class = MPAARatingSerializer
    permission_classes = (IsStaffOrReadOnly, )


class TypeViewSet(ModelViewSet):
    """
    View set for managing anime type objects.

    Attributes:
        queryset (QuerySet): The queryset of all anime type objects.
        serializer_class (Serializer): The serializer class used for serializing/deserializing anime type data.
        permission_classes (tuple): The permission classes applied to the view set.
    """
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = (IsStaffOrReadOnly, )


class StatusViewSet(ModelViewSet):
    """
    View set for managing anime status objets.

    Attributes:
        queryset (QuerySet): The queryset of all anime status objects.
        serializing_class (Serializer): The serializer class used for serializing/deserializing anime status data.
        permission_classes (tuple): The permission classes applied to the view set.
    """
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = (IsStaffOrReadOnly, )


class OriginModelViewSet(ModelViewSet):
    """
    View set for managing anime origin objects.

    Attributes:
        queryset (QuerySet): The queryset of all anime origin objects.
        serializing_class (Serializer): The serializer class used for serializing/deserializing anime origin data.
        permission_classes (tuple): The permission classes applied to the view set.
    """
    queryset = Origin.objects.all()
    serializer_class = OriginSerializer
    permission_classes = (IsStaffOrReadOnly, )


class ScreenshotViewSet(ModelViewSet):
    """
    View set for managing anime screenshots (frames).

    Attributes:
        queryset (QuerySet): The queryset of all anime screenshots (frames) objects.
        serializing_class (Serializer): The serializer class used for serializing/deserializing anime screenshots data.
        permission_classes (tuple): The permission classes applied to the view set.
    """
    queryset = Screenshot.objects.all()
    serializer_class = ScreenshotSerializer
    permission_classes = (IsStaffOrReadOnly, )


class AnimeRatingViewSet(ModelViewSet):
    """
    View set for managing anime rating.

    Attributes:
        queryset (QuerySet): The queryset of all anime rating objects.
        serializing_class (Serializer): The serializer class used for serializing/deserializing anime rating data.
        permission_classes (tuple): The permission classes applied to the view set.
    """
    queryset = AnimeRating.objects.all()
    serializer_class = AnimeRatingSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class AnimeUserCommentViewSet(ModelViewSet):
    """
    View set for managing user comments for anime.

    Attributes:
        queryset (QuerySet): The queryset of all anime user comments objects.
        serializing_class (Serializer): The serializer class used for serializing/deserializing anime user comments.
        permission_classes (tuple): The permission classes applied to the view set.
    """
    queryset = AnimeUserComment.objects.all()
    serializer_class = AnimeUserCommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def list(self, request):
        """
        Returns a list of all user comments.

        Returns:
            Response: The serialized data of the list of user comments.
        """
        queryset = self.queryset.prefetch_related('reply').select_related('likes', 'dislikes').all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class AnimeReviewViewSet(ModelViewSet):
    """
    View set for managing anime reviews objects.

    Attributes:
        queryset (QuerySet): The queryset of all anime review objects.
        serializer_class (Serializer): The serializer class used for serializing/deserializing anime reviews.
        permission_classes (tuple): The permission classes applied to the view set.
    """
    queryset = AnimeReview.objects.all()
    serializer_class = AnimeReviewSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class AnimeBookmarkListViewSet(ModelViewSet):
    """
    View set for managing anime bookmark list objects.

    Attributes:
        queryset (QuerySet): The queryset of all anime bookmark list objects.
        serializer_class (Serializer): The serializer class used for serializing/deserializing anime bookmarks.
        permission_classes (tuple): The permission classes applied to the view set.
    """
    queryset = AnimeBookmarkList.objects.all()
    serializer_class = AnimeBookmarkListSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def list(self, request):
        """
        Returns a list of all anime bookmark list objects.

        Return:
            Response: The serialized data of the list of bookmark lists.
        """
        queryset = self.queryset.prefetch_related('anime')
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class CommentLikeViewSet(ModelViewSet):
    """
    View set for managing comment likes objects.

    Attributes:
        queryset (QuerySet): The queryset of all comment likes.
        serializer_class (Serializer): The serializer class used for serializing/deserializing comment likes.
        permission_classes (tuple): The permission classes applied to the view set.
    """
    queryset = CommentLike.objects.all()
    serializer_class = CommentLikeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class CommentDislikeViewSet(ModelViewSet):
    """
    View set for managing comment dislikes objects.

    Attributes:
        queryset (QuerySet): The queryset of all comment dislikes.
        serializer_class (Serializer): The serializer class used for serializing/deserializing comment dislikes.
        permission_classes (tuple): The permission classes applied to the view set.
    """
    queryset = CommentDislike.objects.all()
    serializer_class = CommentDislikeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
