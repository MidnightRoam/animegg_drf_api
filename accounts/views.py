from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

from .models import CustomUser


class UserModelViewSet(ModelViewSet):
    """User object model view set"""
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['post'])
    def add_friend(self, request, pk=None) -> Response:
        """Add a friend to current logged user"""
        if request.user.is_authenticated:
            try:
                current_user = request.user
                friend_user = self.queryset.get(pk=pk)
                current_user.friends.add(friend_user)
                return Response({'message': 'Friend added successfully'}, status=status.HTTP_200_OK)
            except CustomUser.DoesNotExist:
                return Response("User not found")
            except Exception as e:
                return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({'message': 'You must be logged into to add a new friend'})

    @action(detail=True, methods=['post'])
    def delete_friend(self, request, pk=None) -> Response:
        """Remove a friend from current logged user list"""
        if request.user.is_authenticated:
            try:
                current_user = request.user
                friend_user = self.queryset.get(pk=pk)
                current_user.friends.remove(friend_user)
                return Response({'message': 'Friend removed successfully'})
            except CustomUser.DoesNotExist:
                return Response("User not found")
            except Exception as e:
                return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({'message': 'You must be logged into to remove a friend'})
