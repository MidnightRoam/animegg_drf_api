from rest_framework.routers import DefaultRouter

from .views import (
    MangaModelViewSet,
    TypeModelViewSet,
    StatusModelViewSet,
    GenreModelViewSet
)

router = DefaultRouter()
router.register('all', MangaModelViewSet, basename='manga')
router.register('types', TypeModelViewSet, basename='manga-type')
router.register('statuses', StatusModelViewSet, basename='manga-status')
router.register('genres', GenreModelViewSet, basename='manga-genre')

urlpatterns = [

]

urlpatterns += router.urls
