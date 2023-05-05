from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AnimeViewSet, GenreViewSet

router = DefaultRouter()
router.register(r'all', AnimeViewSet, basename='all')
router.register(r'genres', GenreViewSet, basename='genres')

urlpatterns = [

]

urlpatterns += router.urls
