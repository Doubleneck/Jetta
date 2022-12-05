import re


def _validate_username(username):
    if len(username) < 3:
        raise Exception("Username must be at least 3 letters long")

    if len(username) > 35:
        raise Exception("Username must be at most 35 letters long")

    # Allow `@` and `.` for email usernames
    if not re.match("[a-zA-Z0-9@.]+", username):
        raise Exception("Username contains invalid characters")

    return None  # for clarity


def _validate_password(password):
    if len(password) < 7:
        raise Exception("Password must be at least 7 characters long")

    # Let passwords contain whatever, as long as they contain at least one
    # number, one lowercase letter and one uppecase letter.
    if not any(letter.islower() for letter in password):
        raise Exception("Password must contain at least one lowercase letter")

    if not any(letter.isupper() for letter in password):
        raise Exception("Password must contain at least one uppercase letter")

    if not any(letter.isnumeric() for letter in password):
        raise Exception("Password must contain at least one number")

    return None


def validate_credentials(username, password, repeated_password = None):
    """Checks if the username and password should be
    considered valid.

    Args:
        username (str): The username
        password (str): The password
        repeated_password (str | None): The password again (optional)

    Returns:
        String | None: None if credentials are valid, or
        a string representing the issue otherwise.
    """

    if not repeated_password is None and password != repeated_password:
        raise Exception("Password and password confirmation do not match")

    _validate_username(username)
    _validate_password(password)
    return True
