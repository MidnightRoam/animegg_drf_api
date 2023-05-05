from django.contrib import admin

from .models import (
    Anime,
    Genre,
    AgeValue,
    AgeRestriction
)


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'slug',)


@admin.register(AgeRestriction)
class AgeRestrictionAdmin(admin.ModelAdmin):
    list_display = ('age', 'abbreviation', 'title',)


admin.site.register(Genre)
admin.site.register(AgeValue)
