from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

from characters.models import Character
from .model_helpers import slug_generator
from accounts.models import CustomUser


class Anime(models.Model):
    """Anime object model"""
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

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slug_generator(self.title)
        super().save(*args, **kwargs)


class Genre(models.Model):
    """Genre of anime model"""
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    slug = models.SlugField(editable=False, default='')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slug_generator(self.title)
        super().save(*args, **kwargs)


class AgeValue(models.Model):
    """Age values for age restrictions model"""
    value = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.value)


class AgeRestriction(models.Model):
    """Age restrictions model"""
    age = models.ForeignKey(AgeValue, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(blank=True)
    abbreviation = models.CharField(max_length=2, null=True)
    title = models.CharField(max_length=24, default='')

    def __str__(self):
        if self.age is not None:
            return str(f'{self.age}+')
        return str(self.age)


class MPAARating(models.Model):
    """MPAA age rating model"""
    title = models.CharField(max_length=50, unique=True)
    abbreviation = models.CharField(max_length=5, default='', unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.abbreviation


class Status(models.Model):
    """Anime status model"""
    class StatusValue(models.TextChoices):
        """Status values"""
        ongoing = "Ongoing"
        released = "Released"
        announcement = "Announcement"
    title = models.CharField(choices=StatusValue.choices, default=StatusValue.choices[2], max_length=12, unique=True)
    slug = models.SlugField(editable=False, default='')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slug_generator(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"


class Type(models.Model):
    """Anime type model"""
    class TypeValue(models.TextChoices):
        """Type values"""
        tv_series = 'TV Series', _('TV Series')
        movie = 'Movie'
        ova = 'OVA', _('OVA')
        special = 'Special'
    title = models.CharField(choices=TypeValue.choices, default=TypeValue.choices[0], max_length=10, unique=True)
    slug = models.SlugField(editable=False, default='')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slug_generator(self.title)
        super().save(*args, **kwargs)


class Origin(models.Model):
    """Anime origin value model"""
    title = models.CharField(max_length=124, unique=True, default='')
    slug = models.SlugField(editable=False, default='')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slug_generator(self.title)
        super().save(*args, **kwargs)


class Screenshot(models.Model):
    """Anime screenshot model"""
    anime = models.ForeignKey('Anime', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='anime_screenshots/')


class AnimeBookmarkList(models.Model):
    """Bookmark model"""
    class BookmarkValue(models.TextChoices):
        watched = 'watched', _('Watched')
        watching = 'watching', _('Watching')
        planned = 'planned', _('Planned')
        dropped = 'dropped', _('Dropped')
        postponed = 'postponed', _('Postponed')
        rewatching = 'rewatching', _('Re-watching')
    list = models.CharField(max_length=50, choices=BookmarkValue.choices, default=BookmarkValue.choices[1])
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    anime = models.ManyToManyField(Anime)

    class Meta:
        verbose_name = 'Bookmark list'
        verbose_name_plural = 'Bookmark lists'


class AnimeRatingStar(models.Model):
    """Anime rating star model"""
    value = models.PositiveSmallIntegerField(
        unique=True,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )

    def __str__(self):
        return str(self.value)


class AnimeRating(models.Model):
    """Anime user rating model"""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)
    value = models.ForeignKey(AnimeRatingStar, on_delete=models.CASCADE, default=None)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, default=None, related_name='anime_ratings')

    def save(self, *args, **kwargs):
        existing_reviews = AnimeRating.objects.filter(user=self.user, anime=self.anime)
        if existing_reviews:
            raise Exception({"Error": "You have already left a review"})
        super().save(*args, **kwargs)


class AnimeUserComment(models.Model):
    """User comment for anime"""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, default=None)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    reply = models.ManyToManyField('self')

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class AnimeReview(models.Model):
    """Anime user review"""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, default=None)
    text = models.TextField()
    rate = models.ForeignKey(AnimeRatingStar, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_created=True, null=True)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
