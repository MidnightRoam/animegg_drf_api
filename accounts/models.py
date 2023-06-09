from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from catalog.model_helpers import slug_generator


class CustomUser(AbstractUser):
    """Custom user model"""
    class UserSexChoice(models.TextChoices):
        """User sex choice model"""
        not_specified = 'Not Specified', _('Not Specified')
        female = 'Female', _('Female')
        male = 'Male', _('Male')
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    birthday_date = models.DateField(blank=True, null=True)
    sex = models.CharField(choices=UserSexChoice.choices, max_length=15, default=UserSexChoice.not_specified)
    status = models.CharField(max_length=255, blank=True)
    about = models.TextField(blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='accounts/user_images')
    friends = models.ManyToManyField('self', symmetrical=True, blank=True)
    slug = models.SlugField(default=None, null=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slug_generator(self.username)
        super().save(*args, **kwargs)


class FriendshipRequest(models.Model):
    """
    Friendship user request.

    Attributes:
        from_user (ForeignKey[Customuser]): The user who wants to add in friend list.
        to_user (ForeignKey[Customuser]): The user who received the request.
        created_at (DateTimeField): The created date of the request.
    """
    from_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='friendship_requests_sent')
    to_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='friendship_requests_received')
    created_at = models.DateTimeField(auto_now_add=True)
