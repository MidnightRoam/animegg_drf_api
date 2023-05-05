from rest_framework.serializers import ModelSerializer

from .models import (
    Character
)


class CharacterSerializer(ModelSerializer):
    """Character serializer"""
    class Meta:
        model = Character
        fields = ('id', 'name', 'subname', 'image', 'description', 'slug', )
