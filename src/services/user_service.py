from repositories.user_repository import the_user_repository
from util import validate_credentials

class UserService:
    def __init__(self, repository=the_user_repository):
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

    def get_user_id_by_username(self, username):
        """Search User Id

        Args:
            username (str): Username for user

        Returns:
            id (str): user_id for Username
        """

        return self.user_repository.get_user_id_by_username(username)


the_user_service = UserService()
