from django.db import models
from django.utils.translation import gettext_lazy as _

from manga.models import Manga
from catalog.models import Anime
from catalog.model_helpers import slug_generator


class Author(models.Model):
    """Author model"""
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    subname = models.CharField(max_length=255, blank=True)
    image = models.ImageField(max_length=255, upload_to='author_images/', blank=True)
    manga = models.ManyToManyField(Manga, blank=True)
    anime = models.ManyToManyField(Anime, blank=True)
    slug = models.SlugField(editable=False, default='')
    responsibilities = models.ManyToManyField('Responsibility', blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            full_name = f'{self.first_name} {self.last_name}'
            self.slug = slug_generator(full_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Responsibility(models.Model):
    """Author responsibility model"""
    class ResponsibilitiesChoices(models.TextChoices):
        """Responsibility choices"""
        story = 'Story', _('Story'),
        drawning = 'Drawning', _('Drawning'),
    title = models.CharField(choices=ResponsibilitiesChoices.choices,
                             default=ResponsibilitiesChoices.choices[0],
                             unique=True,
                             max_length=10)

    class Meta:
        verbose_name = 'Responsibility'
        verbose_name_plural = 'Responsibilities'

    def __str__(self):
        return self.title

