from repositories.user_repository import the_user_repository
import re

def _validate_username(username):
    if len(username) < 3:
        return "Username must be at least 3 letters long"

    if len(username) > 35:
        return "Username must be at most 35 letters long"
    
    # Allow `@` and `.` for email usernames
    if not re.match("[a-zA-Z0-9@.]+", username):
        return "Username contains invalid characters"

    return None # for clarity

def _validate_password(password):
    if len(password) < 7:
        return "Password must be at least 7 characters long"

    # Let passwords contain whatever, as long as they contain at least one
    # number, one lowercase letter and one uppecase letter.
    if not any(letter.islower() for letter in password):
        return "Password must contain at least one lowercase letter"
    
    if not any(letter.isupper() for letter in password):
        return "Password must contain at least one uppercase letter"

    if not any(letter.isnumeric() for letter in password):
        return "Password must contain at least one number"

    return None

def validate_credentials(username, password):
    """Checks if the username and password should be
    considered valid.

    Args:
        username (str): The username
        password (str): The password

    Returns:
        String | None: None if both are valid, or
        a string representing the issue otherwise.
    """

    result = _validate_username(username)
    if not result is None:
        return result

    return _validate_password(password)

class UserService:
    def __init__(self, repository = the_user_repository):
        self.user_repository = repository

    def _check_if_user_exists(self, username):
        """Checks if there are users with the username

        Args:
            username (str): Username of the user searched

        Returns:
            Boolean: True if there is already a user, False if not
        """
        return self.user_repository.search_user(username=username)

    def create_user(self, username, password):
        """User creation

        Args:
            username (str): Username for user
            password (str): Password for user

        Returns:
            Boolean: False if there is already a user with the username or
            if the credentials are invalid
        """

        if not validate_credentials(username, password) is None:
            return False

        if self._check_if_user_exists(username=username):
            return False

        self.user_repository.create_user(username=username, password=password)
        return True

    def sign_in(self, username, password):
        """Sign in function

        Args:
            username (str): Username for user
            password (str): Password for user

        Returns:
            Boolean: True if sign in is succesful, False if not.
        """

        return self.user_repository.sign_in(username=username, password=password)

the_user_service = UserService()
