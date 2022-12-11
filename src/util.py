import re
from io import BytesIO
from flask import send_file

def _validate_username(username):
    """Check username is valid and raise exception if username is not valid
    
    Args: 
        username (string)
        
    Returns:
        None: If username is valid
    """

    if len(username) < 3:
        raise Exception("Username must be at least 3 letters long")

    if len(username) > 35:
        raise Exception("Username must be at most 35 letters long")

    # Allow `@` and `.` for email usernames
    if not re.match("[a-zA-Z0-9@.]+", username):
        raise Exception("Username contains invalid characters")

    return None  # for clarity


def _validate_password(password):
    """Check password is valid and raise exception if username is not valid
    
    Args: 
        password (string)
        
    Returns:
        None: If username is valid
    """

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

def send_string_as_file(contents, filename):
    """Sends the string as a file to the user, showing up as a download
    for the user.

    Args:
        contents (str): the file contents as a string
        filename (str): the filename for the download
    
    Returns:
        A response object to return from a route function.
    """

    buffer = BytesIO()
    buffer.write(contents.encode("utf-8"))
    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True, # download, don't open in browser
        download_name=filename,
        mimetype="text/plain"
    )
