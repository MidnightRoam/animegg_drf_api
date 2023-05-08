from django.db import models
from django.utils.translation import gettext_lazy as _

from catalog.model_helpers import slug_generator
from characters.models import Character


class Manga(models.Model):
    """Manga object model"""
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)
    volumes = models.PositiveSmallIntegerField()
    chapters = models.PositiveSmallIntegerField()
    released = models.DateField(blank=True, null=True)
    finished = models.DateField(blank=True, null=True)
    type = models.ForeignKey('Type', on_delete=models.CASCADE)
    slug = models.SlugField(editable=False, default='')
    characters = models.ManyToManyField(Character, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slug_generator(self.title)
        super().save(*args, **kwargs)


class Type(models.Model):
    """Type of manga model"""
    class TypeValue(models.TextChoices):
        """Type values"""
        manga = 'Manga', _('Manga')
        manhwa = 'Manhwa', _('Manhwa')
        manhua = 'Manhua', _('Manhua')
        oneshot = 'One-shot', _('One-shot')
        doujinshi = 'Doujinshi', _('Doujinshi')

    title = models.CharField(choices=TypeValue.choices, default=TypeValue.choices[0], max_length=10, unique=True)
    slug = models.SlugField(editable=False, default='')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slug_generator(self.title)
        super().save(*args, **kwargs)


class Status(models.Model):
    """Manga status model"""
    class StatusValue(models.TextChoices):
        """Status values"""
        ongoing = "Ongoing"
        released = "Released"
        announcement = "Announcement"

    title = models.CharField(choices=StatusValue.choices, default=StatusValue.choices[2], max_length=12,
                             unique=True)
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


class Genre(models.Model):
    """Genre of manga model"""
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    slug = models.SlugField(editable=False, default='')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slug_generator(self.title)
        super().save(*args, **kwargs)
