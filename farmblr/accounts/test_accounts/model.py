from model_bakery import baker
from django.test import TestCase


# Testing models
class TestAccountModels(TestCase):
    def setUp(self):
        self.instance = baker.make('User', username='test_user')
        self.user = baker.make('Profile', user=self.instance)

    def test_profile_str(self):
        self.assertEqual(str(self.user), "test_user")