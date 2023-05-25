from rest_framework.routers import DefaultRouter
from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import (
    UserModelViewSet,
)


router = DefaultRouter()
router.register('users', UserModelViewSet, basename='user')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path(
        'users/<int:pk>/accept_request_to_friendship/',
        UserModelViewSet.as_view({'post': 'accept_request_to_friendship'}),
        name='accept_request_to_friendship'
    ),
    path('users/<int:pk>/remove_friend/', UserModelViewSet.as_view({'post': 'delete_friend'}), name='remove_friend'),
    path(
        'users/<int:pk>/friendship_request/',
        UserModelViewSet.as_view({'post': 'send_request_to_friendship'}),
        name='send_request_to_friendship'
    ),
]

urlpatterns += router.urls
