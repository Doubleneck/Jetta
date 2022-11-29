import unittest

from services.user_service import UserService, validate_credentials
from tests.repositories.user_repository_test import create_test_user_repository

VALID_USERNAME = "Mikko"
VALID_PASSWORD = "Passw0rd"

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.service = UserService(create_test_user_repository())

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
        self.assertFalse(self.service.create_user(VALID_USERNAME, "Some0therValidPassword"))

# validate_credentials() tests
class TestCredentialsValidation(unittest.TestCase):
    def test_valid_username_and_password_is_accepted(self):
        self.assertIsNone(validate_credentials(VALID_USERNAME, VALID_PASSWORD))

    def test_password_must_contain_uppercase_lowercase_and_numeric_letters(self):
        # validate_credentials() returns None only if the credentials were valid
        self.assertIsNotNone(validate_credentials(VALID_USERNAME, "Password")) # missing number
        self.assertIsNotNone(validate_credentials(VALID_USERNAME, "passw0rd")) # missing uppercase letter
        self.assertIsNotNone(validate_credentials(VALID_USERNAME, "P4SSW0RD")) # missing lowercase letter

    def test_password_must_be_at_least_seven_characters_long(self):
        self.assertIsNotNone(validate_credentials(VALID_USERNAME, "Pw0rd"))

    def test_username_must_be_at_least_three_characters_long(self):
        self.assertIsNotNone(validate_credentials("VG", VALID_PASSWORD))

    def test_username_must_be_at_most_35_characters_long(self):
        self.assertIsNotNone(validate_credentials("abcdefghijklmnopqrstuvwxyz0123456789", VALID_PASSWORD)) # 36 long

    def test_emails_are_accepted_as_usernames(self):
        self.assertIsNone(validate_credentials("mikko.mikkonen@mikkomail.com", VALID_PASSWORD))

    def test_invalid_characters_in_username_are_rejected(self):
        self.assertIsNotNone(validate_credentials("$eppo", VALID_PASSWORD))