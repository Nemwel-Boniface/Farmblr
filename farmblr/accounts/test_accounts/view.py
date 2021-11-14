from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from model_bakery import baker
from ..models import Profile

class TestAccountViews(TestCase):
    @classmethod
    def setUpTestData(cls):
        credentials = {
            "username": "test_user",
            "password": "test_password",
        }
        User.objects.create_user(**credentials)

    def test_login__view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_logout_view(self):
        self.client.login(username='test_user', password='test_password')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)