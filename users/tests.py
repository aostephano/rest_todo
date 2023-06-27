from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import User
from .serializers import UserSerializer


class UserViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@example.com')

    def test_create_user(self):
        url = reverse('users:create_user')

        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'testpassword',
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

    def test_get_user(self):
        url = reverse('users:get_user', args=[self.user.pk])

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, UserSerializer(instance=self.user).data)

    def test_update_user(self):
        url = reverse('users:update_user', args=[self.user.pk])

        data = {
            'username': 'updateduser',
            'password': 'testpassword',
            'email': 'updateduser@example.com',
        }

        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, UserSerializer(instance=self.user).data)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updateduser')
        self.assertEqual(self.user.email, 'updateduser@example.com')

    def test_delete_user(self):
        url = reverse('users:delete_user', args=[self.user.pk])

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(User.objects.filter(pk=self.user.pk).exists())
