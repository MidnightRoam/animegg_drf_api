from rest_framework.routers import DefaultRouter

from .views import (
    AnimeViewSet,
    GenreViewSet,
    AgeValueViewSet,
    AgeRestrictionViewSet,
    TypeViewSet,
    StatusViewSet,
    MPAARatingModelViewSet,
    OriginModelViewSet
)

router = DefaultRouter()
router.register(r'all', AnimeViewSet, basename='anime')
router.register(r'genres', GenreViewSet, basename='genre')
router.register(r'age-values', AgeValueViewSet, basename='age-value')
router.register(r'age-restrictions', AgeRestrictionViewSet, basename='age-restriction')
router.register(r'mpaa-ratings', MPAARatingModelViewSet, basename='mpaa-rating')
router.register(r'types', TypeViewSet, basename='type')
router.register(r'statuses', StatusViewSet, basename='status')
router.register(r'origins', OriginModelViewSet, basename='origin')

urlpatterns = [

]

urlpatterns += router.urls
