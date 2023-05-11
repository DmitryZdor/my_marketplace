from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now
from users.models import User
from users.forms import UserRegistrationForm


class UserRegistrationViewTestCase(TestCase):

    def setUp(self):
        self.path = reverse('users:registration')
        self.data = {
            'first_name': 'John', 'last_name': 'Smith', 'username': 'JohnSmith', 'email': 'JohnSmith@net.us',
            'password1': 'John_ty7780&7', 'password2': 'John_ty7780&7',
        }

    def test_user_registration_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'TOPS_CROPS - Регистрация')
        self.assertTemplateUsed(response, 'users/registration.html')

    def test_user_registration_post_success(self):

        username = self.data['username']
        self.assertFalse(User.objects.filter(username=username).exists())
        response = self.client.post(self.path, self.data)
        self.assertTrue(User.objects.filter(username=username).exists())
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('users:login'))