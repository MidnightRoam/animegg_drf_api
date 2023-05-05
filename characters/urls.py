from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    CharacterModelViewSet
)

router = DefaultRouter()
router.register('all', CharacterModelViewSet, basename='character')

urlpatterns = [

]

urlpatterns += router.urls
