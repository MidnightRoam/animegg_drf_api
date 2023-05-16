from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import (
    AnimeViewSet,
    GenreViewSet,
    AgeValueViewSet,
    AgeRestrictionViewSet,
    TypeViewSet,
    StatusViewSet,
    MPAARatingModelViewSet,
    OriginModelViewSet,
    ScreenshotViewSet,
    AnimeRatingViewSet,
    AnimeUserCommentViewSet
)

router = DefaultRouter()
router.register(r'anime', AnimeViewSet, basename='anime')
router.register(r'genres', GenreViewSet, basename='genre')
router.register(r'age-values', AgeValueViewSet, basename='age-value')
router.register(r'age-restrictions', AgeRestrictionViewSet, basename='age-restriction')
router.register(r'mpaa-ratings', MPAARatingModelViewSet, basename='mpaa-rating')
router.register(r'types', TypeViewSet, basename='type')
router.register(r'statuses', StatusViewSet, basename='status')
router.register(r'origins', OriginModelViewSet, basename='origin')
router.register(r'screenshots', ScreenshotViewSet, basename='screenshot')
router.register(r'anime-ratings', AnimeRatingViewSet, basename='anime-rating')
router.register(r'anime-comments', AnimeUserCommentViewSet, basename='anime-user-comment')

router.urls.append(path('random-anime/', AnimeViewSet.as_view({'get': 'get_random_anime'}), name='anime-random'))

urlpatterns = [
    # path('random-anime/', RandomAnimeAPIView.as_view(), name='random-anime')
]

urlpatterns += router.urls
