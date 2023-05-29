from django.db import models
from django.db.models.fields import related
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

from characters.models import Character
from .model_helpers import slug_generator
from accounts.models import CustomUser


class Anime(models.Model):
    """
    Anime object model.

    Attributes:
        title (str): The title of the anime.
        subtitle (str): The subtitle (additional title) of the anime.
        description (str): The description of the anime.
        poster (image): The poster (image) of the anime.
        genres (ManyToManyField[Genre]): The genres of the anime.
        release_date (DateField): The release date of the anime.
        main_characters (ManyToManyField[Character]): The main characters of the anime.
        slug (SlugField): The slugified version of the title.
        mpaa_rating (ManyToManyField[MPAARating]): MPAA rating (additional age restrictions) of the anime.
        age_restrictions (ForeignKey[AgeRestriction]): Age restrictions of the anime.
        status (ForeignKey[Status]): Status (ongoing, released, announced) of the anime.
        type (ForeignKey[Type]): Type (TV series, movie, OVA, special) of the anime.
        origin (ForeignKey[Origin]): Origin (original, novel, manga) of the anime.
        created_at (DateTimeField): Date of publish (creation) of the anime object.
        related_anime (ManyToManyField[self]): Related anime objects.
        is_published (bool): Boolean indicating whether anime object is published.
    """
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    poster = models.ImageField(upload_to='anime_posters/', blank=True)
    genres = models.ManyToManyField('Genre', blank=True)
    release_date = models.DateField(blank=True, null=True)
    main_characters = models.ManyToManyField(Character, blank=True, related_name='anime_characters')
    slug = models.SlugField(editable=False, default='')
    mpaa_rating = models.ForeignKey('MPAARating', on_delete=models.CASCADE, blank=True, null=True)
    age_restrictions = models.ForeignKey('AgeRestriction', on_delete=models.CASCADE, blank=True, null=True)
    status = models.ForeignKey('Status', on_delete=models.CASCADE, null=True, blank=True)
    type = models.ForeignKey('Type', on_delete=models.CASCADE, null=True)
    origin = models.ForeignKey('Origin', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    related_anime = models.ManyToManyField('self', blank=True, symmetrical=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        """
        Return a string representation of anime.
        """
        return self.title

    def save(self, *args, **kwargs):
        """
        Save the anime instance.

        If the slug is not set yet, generate a slug from the title,
        using slug_generator function from model_helpers.py module.
        """
        if not self.slug:
            self.slug = slug_generator(self.title)
        super().save(*args, **kwargs)


class Genre(models.Model):
    """
    Genre of anime model.

    Attributes:
        title (str): The title of the genre.
        description (str): The description of the genre.
        slug (str): The slugified version of the title.
    """
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    slug = models.SlugField(editable=False, default='')

    def __str__(self):
        """
        Return a string representation of the genre.
        """
        return self.title

    def save(self, *args, **kwargs):
        """
        Save the genre instance.

        If the slug is not set yet, generate a slug from the title,
        using slug_generator function from model_helpers.py module.
        """
        if not self.slug:
            self.slug = slug_generator(self.title)
        super().save(*args, **kwargs)


class AgeValue(models.Model):
    """
    Age values for age restrictions model

    Attributes:
        value (int): The value of the age.
    """
    value = models.PositiveSmallIntegerField()

    def __str__(self):
        """
        Return a string representation of the value.
        """
        return str(self.value)


class AgeRestriction(models.Model):
    """
    Age restrictions model.

    Attributes:
        age (ForeignKey[AgeValue]): age value for the age restriction.
        description (str): description for the age restriction.
        abbreviation (str): abbreviation for the age restriction.
        title (str): title for the age restriction.
    """
    age = models.ForeignKey(AgeValue, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(blank=True)
    abbreviation = models.CharField(max_length=2, null=True)
    title = models.CharField(max_length=24, default='')

    def __str__(self):
        """
        Return a string representation of the value.

        If the age is greater than 0, then the method will return a value with a + sign
        and without otherwise.
        """
        if self.age is not None:
            return str(f'{self.age}+')
        return str(self.age)


class MPAARating(models.Model):
    """
    MPAA age rating model.

    Attributes:
        title (str): title for the age restriction.
        abbreviation (str): abbreviation for the MPAA rating.
        description (str): description for the MPAA rating.
    """
    title = models.CharField(max_length=50, unique=True)
    abbreviation = models.CharField(max_length=5, default='', unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        """
        Return a string representation of the age abbreviation
        """
        return self.abbreviation


class Status(models.Model):
    """
    Anime status model.

    Attributes:
        title (str): Title for the status (ongoing, released, announcement).
        slug (SlugField): slugified version of the title.
    """
    class StatusValue(models.TextChoices):
        """Status values"""
        ongoing = "Ongoing"
        released = "Released"
        announcement = "Announcement"
    title = models.CharField(choices=StatusValue.choices, default=StatusValue.choices[2], max_length=12, unique=True)
    slug = models.SlugField(editable=False, default='')

    def __str__(self):
        """
        Return a string representation of the status title
        """
        return self.title

    def save(self, *args, **kwargs):
        """
        Save the status instance.

        If slug is empty, then he automatically generated using
        slug_generator function from model_helpers.py module.
        """
        if not self.slug:
            self.slug = slug_generator(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"


class Type(models.Model):
    """
    Anime type model.

    Attributes:
        title (str): Title of the status (TV Series, Movie, OVA, Special).
        slug (SlugField): Slugified version of the status title.
    """
    class TypeValue(models.TextChoices):
        """Type values"""
        tv_series = 'TV Series', _('TV Series')
        movie = 'Movie'
        ova = 'OVA', _('OVA')
        special = 'Special'
    title = models.CharField(choices=TypeValue.choices, default=TypeValue.choices[0], max_length=10, unique=True)
    slug = models.SlugField(editable=False, default='')

    def __str__(self):
        """
        String representation of the status title
        """
        return self.title

    def save(self, *args, **kwargs):
        """
        Save the status instance.

        If slug is empty, then he automatically generated using
        slug_generator function from model_helpers.py module.
        """
        if not self.slug:
            self.slug = slug_generator(self.title)
        super().save(*args, **kwargs)


class Origin(models.Model):
    """
    Anime origin value model.

    Attributes:
        title (str): Title of the origin.
        slug (SlugField): Slugified version of the origin title.
    """
    title = models.CharField(max_length=124, unique=True, default='')
    slug = models.SlugField(editable=False, default='')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slug_generator(self.title)
        super().save(*args, **kwargs)


class Screenshot(models.Model):
    """
    Anime screenshot model.

    Attributes:
        anime (ForeignKey[Anime]): Related anime.
        image (image): Screenshot (frame).
    """
    anime = models.ForeignKey('Anime', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='anime_screenshots/')


class AnimeBookmarkList(models.Model):
    """
    Bookmark model.

    Attributes:
        title (str): title of the anime bookmark.
        user (CustomUser): bookmark user associated.
        anime (ManyToMany[Anime]): anime which has been added to the bookmark.
    """
    class BookmarkValue(models.TextChoices):
        watched = 'watched', _('Watched')
        watching = 'watching', _('Watching')
        planned = 'planned', _('Planned')
        dropped = 'dropped', _('Dropped')
        postponed = 'postponed', _('Postponed')
        rewatching = 'rewatching', _('Re-watching')
    title = models.CharField(max_length=50, choices=BookmarkValue.choices, default=BookmarkValue.choices[1])
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    anime = models.ManyToManyField(Anime)

    class Meta:
        verbose_name = 'Bookmark list'
        verbose_name_plural = 'Bookmark lists'


class AnimeRatingStar(models.Model):
    """
    Anime rating star model.

    Attributes:
        value (int): The rating star value.
    """
    value = models.PositiveSmallIntegerField(
        unique=True,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )

    def __str__(self):
        """
        String representation of the rating star value
        """
        return str(self.value)


class AnimeRating(models.Model):
    """
    Anime user rating model.

    Attributes:
        user (CustomUser): user which rated the anime.
        value (ForeignKey[AnimeRatingStar]): rating value.
        anime (Foreign[Anime]): anime which has been rated.
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)
    value = models.ForeignKey(AnimeRatingStar, on_delete=models.CASCADE, default=None)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, default=None, related_name='anime_ratings')

    def save(self, *args, **kwargs):
        """
        Save the anime rating instance.

        If anime already rated, it returns an exception.
        """
        existing_reviews = AnimeRating.objects.filter(user=self.user, anime=self.anime)
        if existing_reviews:
            raise Exception({"Error": "You have already left a review"})
        super().save(*args, **kwargs)


class AnimeUserComment(models.Model):
    """
    User comment for anime model.

    Attributes:
        user (CustomUser): User which left the comment.
        anime (ForeignKey[Anime]): Anime where the user left the comment.
        text (str): Comment text.
        created_at (DateTimeField): Creation comment date.
        reply (ManyToMany[self]): Replies from other users to root comment.
        likes (ForeignKey[CommentLike]): Count of likes under the comment.
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, default=None)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    reply = models.ManyToManyField('self')
    likes = models.ForeignKey('CommentLike',
                              on_delete=models.CASCADE,
                              editable=False,
                              blank=True,
                              null=True,)
    dislikes = models.ForeignKey('CommentDislike',
                              on_delete=models.CASCADE,
                              editable=False,
                              blank=True,
                              null=True,)

    def __str__(self):
        """
        String representation of anime user comment
        """
        return str(self.user)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class AnimeReview(models.Model):
    """
    Anime user review model.

    Attributes:
        user (CustomUser): User which left the anime review.
        anime (ForeignKey[Anime]): Reviewed anime.
        text (str): Comment text.
        rate (ForeignKey[AnimeRating]): Rate value.
        created_at (DateTimeField): Review creation date.
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, default=None)
    text = models.TextField()
    rate = models.ForeignKey(AnimeRatingStar, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_created=True, null=True)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'


class CommentLike(models.Model):
    """
    Like object for user comment.

    Attributes:
        comment (ForeignKey[AnimeUserComment]): Comment object.
        user (CustomUser): User which liked comment.
    """
    comment = models.ForeignKey(AnimeUserComment, on_delete=models.CASCADE, related_name='comment_likes')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class CommentDislike(models.Model):
    """
    Dislike object for user comment.

    Attributes:
        comment (ForeignKey[AnimeUserComment]): Comment object.
        user (CustomUser): User which disliked comment.
    """
    comment = models.ForeignKey(AnimeUserComment, on_delete=models.CASCADE, related_name='comment_dislikes')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
