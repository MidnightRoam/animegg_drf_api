from django.db.models import Avg, Prefetch
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import (
    Anime,
    Genre,
    AgeRestriction,
    Type,
    Status,
    AgeValue,
    MPAARating,
    Origin,
    Screenshot,
    AnimeRating,
    AnimeUserComment,
    AnimeReview,
    AnimeBookmarkList,
    CommentLike
)
from characters.serializers import CharacterSerializer
from video_player.serializers import EpisodeSerializer


class ScreenshotSerializer(ModelSerializer):
    """
    Serializer for anime screenshots.

    Fields:
        - id: The unique identifier for the screenshot.
        - anime: Screenshot (frame) from the anime.
        - image: Image of the screenshot (frame).
    """
    class Meta:
        model = Screenshot
        fields = ('id', 'anime', 'image')


class AnimeSerializer(ModelSerializer):
    """
    Serializer for anime objects.

    Fields:
        - id: The unique identifier of the anime.
        - title: The title of the anime.
        - subtitle: The subtitle (additional title) of the anime.
        - description: The description of the anime.
        - poster: The poster (image) of the anime.
        - main_characters: Anime main characters.
        - release_date: The release date of the anime.
        - genres: The anime genres.
        - origin: The original source of the work.
        - slug: The slugified version of the title.
        - age_restrictions: The anime age restrictions.
        - mpaa_rating: The anime MPAA rating (additional age restrictions).
        - type: The type of anime.
        - status: The status of anime (released, ongoing, announced).
        - screenshot_set: The set of anime screenshots (frames).
        - rating: The average user rating of anime.
        - related_anime: Related anime objects.
        - episode_set: The set of anime episodes for video player.
    """
    main_characters = serializers.SerializerMethodField()
    genres = serializers.SerializerMethodField()
    age_restrictions = serializers.SerializerMethodField()
    screenshot_set = ScreenshotSerializer(many=True, required=False)
    episode_set = EpisodeSerializer(many=True, required=False)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Anime
        fields = (
            'id',
            'title',
            'subtitle',
            'description',
            'poster',
            'main_characters',
            'release_date',
            'genres',
            'origin',
            'slug',
            'age_restrictions',
            'mpaa_rating',
            'type',
            'status',
            'screenshot_set',
            'rating',
            'related_anime',
            'episode_set',
        )

    def get_main_characters(self, obj):
        """ORM query optimization for main characters field"""
        main_characters = obj.main_characters.all()
        serializer = CharacterSerializer(main_characters, many=True)
        return serializer.data

    def get_genres(self, obj):
        """ORM query optimization for genres field"""
        genres = obj.genres.all()
        serializer = GenreSerializer(genres, many=True)
        return serializer.data

    def get_age_restrictions(self, obj):
        """ORM query optimization for age restrictions field"""
        age_restrictions = obj.age_restrictions
        serializer = AgeRestrictionSerializer(age_restrictions, many=False)
        return serializer.data

    def get_screenshot_set(self, obj):
        """ORM query optimization for anime screenshots"""
        screenshot_set = obj.screenshots
        serializer = ScreenshotSerializer(screenshot_set, many=True)
        return serializer.data

    def get_rating(self, obj) -> float or None:
        """Returns average rating for anime as a float field"""
        ratings = Anime.objects.annotate(avg_rating=Avg('anime_ratings__value')).filter(id=obj.id).first()
        if ratings is not None:
            return ratings.avg_rating
        return None

    def get_episode_set(self, obj):
        """ORM query optimization for anime episodes"""
        episode_set = obj.episode
        serializer = EpisodeSerializer(episode_set, many=True)
        return serializer.data


class GenreSerializer(ModelSerializer):
    """
    Serializer for anime genres.

    Fields:
        - id: The unique identifier of genre.
        - title: The title of the genre.
        - description: The description of the genre.
        - slug: The slugified version of the title.
    """
    class Meta:
        model = Genre
        fields = ('id', 'title', 'description', 'slug',)


class AgeValueSerializer(ModelSerializer):
    """
    Serializer for age values for age restrictions.

    Fields:
        - id: The unique identifier of age value.
        - value: The age value.
    """
    class Meta:
        model = AgeValue
        fields = ('id', 'value')


class AgeRestrictionSerializer(ModelSerializer):
    """
    Serializer for age restrictions.

    Fields:
        - id: The unique identifier of the age restriction.
        - age: The age of the age restriction.
        - description: The description of the age restriction.
        - abbreviation: The abbreviation of the age restriction.
        - title: The title of the age restriction.
    """
    class Meta:
        model = AgeRestriction
        fields = ('id', 'age', 'description', 'abbreviation', 'title')


class MPAARatingSerializer(ModelSerializer):
    """
    Serializer for the "MPAA" age rating of the anime.

    Fields:
        - id: The unique identifier of the MPAA rating value.
        - title: The title of the MPAA rating value.
        - abbreviation: The abbreviation of the MPAA rating value.
        - description: The text description of the MPAA rating value.
    """
    class Meta:
        model = MPAARating
        fields = ('id', 'title', 'abbreviation', 'description')


class TypeSerializer(ModelSerializer):
    """
    Serializer for type of anime.

    Fields:
        - id: The unique identifier of the type.
        - title: The title of the type.
        - slug: The slugified version of the title
    """
    class Meta:
        model = Type
        fields = ('id', 'title', 'slug',)


class StatusSerializer(ModelSerializer):
    """
    Serializer for anime status.

    Fields:
        - id: The unique identifier for the status.
        - title: The title of the status.
        - slug: The slugified version of the title.
    """
    class Meta:
        model = Status
        fields = ('id', 'title', 'slug',)


class OriginSerializer(ModelSerializer):
    """
    Serializer for origin of anime.

    Fields:
        - id: The unique identifier for the origin.
        - title: The title of the origin.
        - slug: The slugified version of the title.
    """
    class Meta:
        model = Origin
        fields = ('id', 'title', 'slug', )


class AnimeRatingSerializer(ModelSerializer):
    """
    Serializer for anime rating.

    Fields:
        - id: The unique identifier for the anime rating.
        - user: The user who rated the anime.
        - anime: The anime that was rated.
        - value: The value of the rate.
    """
    class Meta:
        model = AnimeRating
        fields = ('id', 'user', 'anime', 'value')


class CommentLikeSerializer(ModelSerializer):
    """
    Serializer for user comment like.

    Fields:
        - id: The unique identifier for the comment like.
        - comment: The comment that was liked.
        - user: The user who liked the comment.
    """
    class Meta:
        model = CommentLike
        fields = ('id', 'comment', 'user')

    def create(self, validated_data):
        user = validated_data['user']
        comment = validated_data['comment']

        try:
            like = CommentLike.objects.get(user=user, comment=comment)  # if comment already liked by user
            like.delete()  # remove like from comment
        except CommentLike.DoesNotExist:  # else
            like = CommentLike.objects.create(user=user, comment=comment)  # like comment

        return like


class AnimeUserCommentSerializer(ModelSerializer):
    """
    Serializer for anime user comments.

    Fields:
        - id: The unique identifier for the comment.
        - user: The user who left the comment.
        - anime: The anime where comment was left.
        - text: The text of the comment.
        - reply: The reply from other users to the comment.
        - likes: The comment likes.
    """
    likes = serializers.SerializerMethodField()

    class Meta:
        model = AnimeUserComment
        fields = ('id', 'user', 'anime', 'text', 'reply', 'likes')

    def get_likes(self, obj) -> int:
        """Return a int of comment likes"""
        return obj.comment_likes.count()


class AnimeReviewSerializer(ModelSerializer):
    """
    Serializer for anime user reviews.

    Fields:
        - id: The unique identifier for the review.
        - user: The user who left the review.
        - anime: The anime which reviewed by a user.
        - rate: The rate of the review.
        - text: The text of review.
        - created_at: Date the published review was created.
    """
    class Meta:
        model = AnimeReview
        fields = ('id', 'user', 'anime', 'rate', 'text', 'created_at')


class AnimeBookmarkListSerializer(ModelSerializer):
    """
    Serializer for the user bookmarks of anime.

    Fields:
        - id: The unique identifier for the user bookmark.
        - title: The name of the bookmark.
        - user: The creator (user) of the bookmark.
        - anime: Anime bookmarked.
    """
    class Meta:
        model = AnimeBookmarkList
        fields = ('id', 'title', 'user', 'anime', )

