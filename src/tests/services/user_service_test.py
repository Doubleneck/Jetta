import unittest

from services.user_service import UserService
from tests.repositories.user_repository_test import create_test_user_repository


class TestUserService(unittest.TestCase):
    def setUp(self):
        self.service = UserService(create_test_user_repository())

    def test_sign_in_works_after_creating_user(self):
        self.service.create_user("Username", "Password")
        self.assertTrue(self.service.sign_in("Username", "Password"))

    def test_sign_in_with_unknown_credentials_fails(self):
        self.service.create_user("Username", "Password")
        self.assertFalse(self.service.sign_in("username", "Password"))
        self.assertFalse(self.service.sign_in("Username", "password"))

    def test_create_user_with_existing_username_fails(self):
        self.assertTrue(self.service.create_user("Username", "Password"))
        self.assertFalse(self.service.create_user("Username", "Password"))
        self.assertFalse(self.service.create_user("Username", "Password2"))
