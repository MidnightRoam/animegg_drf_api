from django.contrib import admin

from .models import (
    Anime,
    Genre,
    AgeValue,
    AgeRestriction,
    Status,
    Type
)


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    """Anime object admin"""
    list_display = ('title', 'release_date', 'slug',)


@admin.register(AgeRestriction)
class AgeRestrictionAdmin(admin.ModelAdmin):
    """Age restrictions admin"""
    list_display = ('age', 'abbreviation', 'title',)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    """Anime status admin"""
    list_display = ('title', )


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    """Anime type admin"""
    list_display = ('title', )


admin.site.register(Genre)
admin.site.register(AgeValue)
