from rest_framework.reverse import reverse as api_reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AuthenticationTest(APITestCase):
    """
    User authentication test cases
    """

    def setUp(self):
        """
        Method for setting up user
        """
        self.url = api_reverse('authentication:user-registration')
        self.user = {
            'username': 'janeDoe',
            'email': 'jane@doe.com',
            'password': 'janedoe123',
        }

    def test_user_signup_succeed(self):
        """
        Test API can successfully register a new user
        """
        response = self.client.post(self.url, self.user, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    