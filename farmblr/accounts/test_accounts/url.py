from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import *


class TestUrls(SimpleTestCase):
    def test_login_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login_)

    def test_logout_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logout)

    def test_signup_resolved(self):
        url = reverse('signup')
        self.assertEquals(resolve(url).func, sign_up)
