from django.db import models
from django.utils.translation import gettext_lazy as _

from characters.models import Character
from .model_helpers import slug_generator


class Anime(models.Model):
    """Anime object model"""
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    poster = models.ImageField(upload_to='anime_posters/', blank=True)
    genres = models.ManyToManyField('Genre', blank=True)
    release_date = models.DateField(blank=True, null=True)
    main_characters = models.ManyToManyField(Character, blank=True)
    slug = models.SlugField(editable=False, default='')
    mpaa_rating = models.ForeignKey('MPAARating', on_delete=models.CASCADE, blank=True, null=True)
    age_restrictions = models.ForeignKey('AgeRestriction', on_delete=models.CASCADE, blank=True, null=True)
    status = models.ForeignKey('Status', on_delete=models.CASCADE, null=True, blank=True)
    type = models.ForeignKey('Type', on_delete=models.CASCADE, null=True)
    origin = models.ForeignKey('Origin', on_delete=models.CASCADE, null=True)

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

