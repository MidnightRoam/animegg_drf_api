from django.db import models


class Character(models.Model):
    """Character model"""
    name = models.CharField(max_length=255)
    subname = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to='characters_images/', blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.description:
            self.description = 'No description'
        super().save(*args, **kwargs)


