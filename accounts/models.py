from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


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
    sex = models.CharField(choices=UserSexChoice.choices, default=UserSexChoice.choices[0], max_length=15)
    status = models.CharField(max_length=255, blank=True)
    about = models.TextField(blank=True)
