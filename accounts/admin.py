from django.contrib import admin

from .models import CustomUser, FriendshipRequest


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """Custom user admin"""
    list_display = ('username', 'id', )


@admin.register(FriendshipRequest)
class FriendshipRequestAdmin(admin.ModelAdmin):
    """FriendshipRequest admin"""
    list_display = ('id', 'from_user', 'to_user')
