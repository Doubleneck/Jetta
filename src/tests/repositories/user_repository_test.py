import unittest

from repositories.user_repository import UserRepository
from database import Database

def create_test_user_repository():
    database = Database(path = ":memory:")
    database.connect()
    database.initialize_database()
    return UserRepository(database.connection)

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.repository = create_test_user_repository()


