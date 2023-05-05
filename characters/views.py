from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import (
    Character
)

from .serializers import (
    CharacterSerializer
)


class CharacterModelViewSet(ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

