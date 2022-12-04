import unittest

from services.user_service import UserService, validate_credentials
from tests.repositories.user_repository_test import create_test_user_repository

VALID_USERNAME = "Mikko"
VALID_PASSWORD = "Passw0rd"

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.service = UserService(create_test_user_repository())

    def test_creating_user_with_valid_credentials_works(self):
        self.assertTrue(self.service.create_user(VALID_USERNAME, VALID_PASSWORD))

    def test_creating_user_with_invalid_credentials_fails(self):
        # Note: credential-validation tests are done in depth in util_test.py;
        # suffices to verify that the validation function is likely being called.
        self.assertFalse(self.service.create_user("$", VALID_PASSWORD))
        self.assertFalse(self.service.create_user(VALID_USERNAME, "$"))

    def test_sign_in_works_after_creating_user(self):
        self.service.create_user(VALID_USERNAME, VALID_PASSWORD)
        self.assertTrue(self.service.sign_in(VALID_USERNAME, VALID_PASSWORD))

    def test_sign_in_with_unknown_credentials_fails(self):
        self.service.create_user(VALID_USERNAME, VALID_PASSWORD)
        self.assertFalse(self.service.sign_in("username", VALID_PASSWORD))
        self.assertFalse(self.service.sign_in(VALID_USERNAME, "password"))

    def test_create_user_with_existing_username_fails(self):
        self.assertTrue(self.service.create_user(VALID_USERNAME, VALID_PASSWORD))
        self.assertFalse(self.service.create_user(VALID_USERNAME, VALID_PASSWORD))
        self.assertFalse(self.service.create_user(VALID_USERNAME, "SomeVal1dPassword"))

    def test_getting_user_id_for_existing_user_returns_int(self):
        self.service.create_user(VALID_USERNAME, VALID_PASSWORD)

        id = self.service.get_user_id_by_username(VALID_USERNAME)
        self.assertTrue(isinstance(id, int))

    def test_getting_user_id_for_nonexisting_user_returns_none(self):
        id = self.service.get_user_id_by_username(VALID_USERNAME)

        self.assertIsNone(id)

    def test_user_id_for_two_different_users_is_different(self):
        self.service.create_user("Mikko", VALID_PASSWORD)
        self.service.create_user("Pekka", VALID_PASSWORD)

        mikkos_id = self.service.get_user_id_by_username("Mikko")
        pekkas_id = self.service.get_user_id_by_username("Pekka")
        self.assertNotEqual(mikkos_id, pekkas_id)