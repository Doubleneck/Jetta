
import unittest
from util import validate_credentials
from tests.services.user_service_test import VALID_PASSWORD, VALID_USERNAME 

# validate_credentials() tests
class TestCredentialsValidation(unittest.TestCase):
    def test_valid_username_and_password_is_accepted(self):
        self.assertTrue(validate_credentials(VALID_USERNAME, VALID_PASSWORD))

    def test_password_must_contain_uppercase_lowercase_and_numeric_letters(self):
        # validate_credentials() returns None only if the credentials were valid
        
        # 1: missing number, 2: missing uppercase letter, 3: missing lowercase letter
        self.assertRaises(Exception, lambda: validate_credentials(VALID_USERNAME, "Password"))
        self.assertRaises(Exception, lambda: validate_credentials(VALID_USERNAME, "passw0rd")) 
        self.assertRaises(Exception, lambda: validate_credentials(VALID_USERNAME, "P4SSW0RD")) 

    def test_password_must_be_at_least_seven_characters_long(self):
        self.assertRaises(Exception, lambda: validate_credentials(VALID_USERNAME, "Pw0rd"))

    def test_username_must_be_at_least_three_characters_long(self):
        self.assertRaises(Exception, lambda: validate_credentials("VG", VALID_PASSWORD))

    def test_username_must_be_at_most_35_characters_long(self):
        long_username = "abcdefghijklmnopqrstuvwxyz0123456789" # 36 long
        self.assertRaises(Exception, lambda: validate_credentials(long_username, VALID_PASSWORD))

    def test_emails_are_accepted_as_usernames(self):
        username = "mikko.mikkonen@mikkomail.com"
        self.assertTrue(validate_credentials(username, VALID_PASSWORD))

    def test_invalid_characters_in_username_are_rejected(self):
        self.assertRaises(Exception, lambda: validate_credentials("$eppo", VALID_PASSWORD))

    def test_password_and_password_repeat_must_match(self):
        self.assertRaises(Exception, lambda:\
                          validate_credentials(VALID_USERNAME, "Passw0rd", "Pass0wrd"))
        self.assertTrue(validate_credentials(VALID_USERNAME, "Passw0rd", "Passw0rd"))
