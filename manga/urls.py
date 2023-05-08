from rest_framework.routers import DefaultRouter

from .views import MangaModelViewSet

router = DefaultRouter()
router.register('all', MangaModelViewSet, basename='manga')

urlpatterns = [

]

urlpatterns += router.urls
