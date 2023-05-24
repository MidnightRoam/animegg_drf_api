from django.contrib import admin

from .models import (
    Anime,
    Genre,
    AgeValue,
    AgeRestriction,
    MPAARating,
    Status,
    Type,
    Origin,
    Screenshot,
    AnimeBookmarkList,
    AnimeRatingStar,
    AnimeRating,
    AnimeUserComment,
    AnimeReview,
    CommentLike,
    CommentDislike
)
from video_player.models import Episode


class EpisodeInLine(admin.TabularInline):
    """Anime episode tabular in line"""
    model = Episode


class ScreenshotInLine(admin.TabularInline):
    """Anime screenshot inline"""
    model = Screenshot


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    """Anime object admin"""
    list_display = ('title', 'release_date', 'slug',)
    inlines = [
        ScreenshotInLine,
        EpisodeInLine
    ]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Genre admin"""
    list_display = ('title', 'slug', 'id')


@admin.register(AgeRestriction)
class AgeRestrictionAdmin(admin.ModelAdmin):
    """Age restrictions admin"""
    list_display = ('age', 'abbreviation', 'title',)


@admin.register(MPAARating)
class MPAARatingAdmin(admin.ModelAdmin):
    """MPAARating admin"""
    list_display = ('title', 'abbreviation', )


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    """Anime status admin"""
    list_display = ('title', 'slug', 'id',)


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    """Anime type admin"""
    list_display = ('title', 'slug')


@admin.register(Origin)
class OriginAdmin(admin.ModelAdmin):
    """Anime origin admin"""
    list_display = ('title', 'slug', 'id')


@admin.register(Screenshot)
class ScreenshotAdmin(admin.ModelAdmin):
    """Anime screenshot admin"""
    list_display = ('anime', 'image', 'id')


admin.site.register(AgeValue)
admin.site.register(AnimeRatingStar)
admin.site.register(AnimeRating)
admin.site.register(AnimeUserComment)
admin.site.register(AnimeReview)
admin.site.register(AnimeBookmarkList)
admin.site.register(CommentLike)
admin.site.register(CommentDislike)
