from rest_framework.routers import DefaultRouter

from .views import (
    AuthorModelViewSet
)

router = DefaultRouter()
router.register('list', AuthorModelViewSet, basename='author')

urlpatterns = [

]

urlpatterns += router.urls
