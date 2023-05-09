from django.contrib import admin

from .models import (
    Author,
    Responsibility
)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Author admin"""
    list_display = ('first_name', 'last_name', 'slug', 'id')


@admin.register(Responsibility)
class ResponsibilitiesAdmin(admin.ModelAdmin):
    """Responsibilities admin"""
    list_display = ('title', 'id')
