from rest_framework.routers import DefaultRouter

from .views import EpisodeModelViewSet

router = DefaultRouter()
router.register('episodes', EpisodeModelViewSet, basename='episode')

urlpatterns = [

]

urlpatterns += router.urls
