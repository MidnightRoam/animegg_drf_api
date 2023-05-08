from django.db import models

from catalog.model_helpers import slug_generator


class Character(models.Model):
    """Character model"""
    name = models.CharField(max_length=255)
    subname = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(editable=False, default='')
    image = models.ImageField(upload_to='characters_images/', blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.description:
            self.description = 'No description'
        if not self.slug:
            self.slug = slug_generator(self.name)
        super().save(*args, **kwargs)


