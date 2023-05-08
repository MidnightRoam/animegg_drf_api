from django.contrib import admin

from .models import (
    Manga,
    Type,
    Status,
    Genre
)


@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    """Manga model admin"""
    list_display = ('title', 'slug', 'id')


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    """Type model admin"""
    list_display = ('title', 'slug', 'id')


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    """Status model admin"""
    list_display = ('title', 'slug', 'id')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Genre model admin"""
    list_display = ('title', 'slug', 'id')