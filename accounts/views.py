from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import CustomUser, FriendshipRequest


class UserModelViewSet(ModelViewSet):
    """
    View set for managing user accounts.

    Attributes:
        queryset (QuerySet): The queryset of all user objects.
        serializer_class (Serializer): The serializer class used for serialization/deserialization users data.
        permission_classes (tuple): The permission classes applied to the view set.
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permissions = (IsAuthenticatedOrReadOnly, )

    def list(self, request):
        """
        Return a list of all users.

        Returns:
            Response: The serialized data of all users.
        """
        queryset = self.queryset.prefetch_related('friends')
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def accept_request_to_friendship(self, request, pk=None) -> Response:
        """
        Accept a friend request for the current logged user.

        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): Friend Request Primary Key.

        Returns:
            Response: The response indicating the status of the request.

        Raises:
            - FriendshipRequest.DoesNotExist: If the request does not exist.
            - Exception: If an unexpected error occurs.

        Notes:
            - This action requires the user to be authenticated.
            - The current user accept a friendship request to the user with the specified primary key.
        """
        if request.user.is_authenticated:
            try:
                current_user = request.user
                friendship_request = FriendshipRequest.objects.get(pk=pk, to_user=current_user)
                current_user.friends.add(friendship_request.from_user)
                friendship_request.delete()
                return Response({'message': 'Friend added successfully'}, status=status.HTTP_200_OK)
            except FriendshipRequest.DoesNotExist:
                return Response("Request not found")
            except Exception as e:
                return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({'message': 'You must be logged into to add a new friend'})

    @action(detail=True, methods=['post'])
    def send_request_to_friendship(self, request, pk=None) -> Response:
        """
        Send a request to establish a friendship with another user.

        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the user to whom the friendship request is sent.

        Returns:
            Response: The response indicating the status of the request.

        Raises:
            - FriendshipRequest.DoesNotExist: If the request does not exist.
            - Exception: If an unexpected error occurs.

        Notes:
            - This action requires the user to be authenticated.
            - The current user sends a friendship request to the user with the specified primary key.
        """
        if request.user.is_authenticated:
            try:
                current_user = request.user
                requested_user = self.queryset.get(pk=pk)
                FriendshipRequest.objects.create(from_user=current_user, to_user=requested_user)
                return Response({'message': 'Request has been sent'})
            except Exception as e:
                return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({'message': 'You must be logged into to remove a friend'})

    @action(detail=True, methods=['post'])
    def delete_friend(self, request, pk=None) -> Response:
        """
        Remove a requested friend from user friend list.

        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the user to be removed from the friends list.

        Returns:
            Response: The response that friend was removed successfully.

        Raises:
            - CustomUser.DoesNotExist: If the requested user does not exist.
            - Exception: If an unexpected error occurs.

        Notes:
            - This action requires the user to be authenticated.
        """
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
