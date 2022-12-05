import unittest

from repositories.note_repository import NoteRepository
from database import Database

def create_test_note_repository():
    database = Database(path = ":memory:")
    database.connect()
    database.initialize_database()
    return NoteRepository(database.connection)

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.repository = create_test_note_repository()
