from django.contrib import admin

from .models import Manga, Type


@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    """Manga model admin"""
    list_display = ('title', 'slug', 'id')


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    """Type model admin"""
    list_display = ('title', 'id')
