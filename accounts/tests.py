from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIRequestFactory

from .models import FriendshipRequest
from .views import UserModelViewSet


class UserModelViewSetTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = UserModelViewSet.as_view({'get': 'list'})
        self.user1 = get_user_model().objects.create(
            username='user1',
            email='user1@example.com'
        )
        self.user2 = get_user_model().objects.create(
            username='user2',
            email='user2@example.com'
        )

    def test_list_users(self):
        """
        Test case to verify that the listing of all users.

        Steps:
        1. Create some user objects.
        2. Make a GET request to retrieve the list of users.
        3. Verify that the status of response is 200 OK.
        4. Assert that the response data contains the expected users.
        """
        request = self.factory.get('/users/')
        request.user = self.user1
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_send_request_to_friendship(self):
        """
        Test case to verify sending a friendship request.

        Steps:
        1. Create a user object.
        2. Make a POST request to sent a friendship request to another user.
        3. Verify that the status of response is 200 OK.
        4. Assert that the friendship request is created successfully.
        """
        request = self.factory.post(f'/users/1/send_request/')
        request.user = self.user1
        view = UserModelViewSet.as_view({'post': 'send_request_to_friendship'})
        response = view(request, pk=1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_accept_request_to_friendship(self):
        """
        Test case to verify accepting a friendship request.

        Steps:
        1. Create a friendship request object.
        2. Make a post request to accept a friendship request.
        3. Verify that the status of response is 200 OK.
        4. Assert that the friend successfully added to friend list.
        """
        friendship_request = FriendshipRequest.objects.create(to_user=self.user1, from_user=self.user2)
        request = self.factory.post(f'/users/1/accept_request/{friendship_request.pk}')
        request.user = self.user1
        view = UserModelViewSet.as_view({'post': 'accept_request_to_friendship'})
        response = view(request, pk=1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_remove_friend(self):
        """
        Test case to verify removing users from a friend list.

        Steps:
        1. Add user2 to friend list of user 1.
        2. Make a post request to a removing a new friend from friend list.
        3. Verify that the status of response is 200 OK.
        4. Assert that the user was successfully removing from friend list.
        """
        self.user1.friends.add(self.user2)
        request = self.factory.post(f'/users/1/remove_friend/{self.user2.pk}')
        request.user = self.user1
        view = UserModelViewSet.as_view({'post': 'delete_friend'})
        response = view(request, pk=self.user2.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

