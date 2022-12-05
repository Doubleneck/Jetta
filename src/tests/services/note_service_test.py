import unittest
from copy import deepcopy
from repositories.note_repository import Note

from services.note_service import NoteService
from tests.repositories.note_repository_test import create_test_note_repository

TEST_USER_ID = 1
TEST_NOTE = Note(
    bib_citekey = "Gregory2009",
    bib_category = "article",
    author = "Keith Gregory and Sue Morón-García",
    title = "Assignment submission, student behaviour and experience",
    year = "2009",
    doi_address = "10.11120/ened.2009.04010016",
)

class TestNoteService(unittest.TestCase):
    def setUp(self):
        self.service = NoteService(create_test_note_repository())

    def test_note_creation_succeeds_with_valid_inputs(self):
        self.assertTrue(self.service.create_note(TEST_USER_ID, TEST_NOTE))

    def test_note_can_be_fetched_once_created(self):
        self.service.create_note(TEST_USER_ID, TEST_NOTE)

        note = self.service.get_all_notes_by_user_id(TEST_USER_ID)[0]
        self.assertEqual(note, TEST_NOTE)

    def test_user_notes_is_empty_before_creating_notes(self):
        notes = self.service.get_all_notes_by_user_id(TEST_USER_ID)
        self.assertEqual(len(notes), 0)

    def test_user_notes_has_length_1_after_inserting_one_note(self):
        self.service.create_note(TEST_USER_ID, TEST_NOTE)

        notes = self.service.get_all_notes_by_user_id(TEST_USER_ID)
        self.assertEqual(len(notes), 1)

    def test_multiple_different_notes_can_be_inserted_for_same_user_id(self):
        self.service.create_note(TEST_USER_ID, TEST_NOTE)
        
        note_2 = Note(
            bib_citekey = "britton",
            bib_category = "article",
            author = "Britton, Bruce and Tesser, Abraham",
            title = "Effects of Time-Management Practices on College Grades",
            year = "1991",
            doi_address = "10.1037/0022-0663.83.3.405",
        )
        self.assertTrue(self.service.create_note(TEST_USER_ID, note_2))

        notes = self.service.get_all_notes_by_user_id(TEST_USER_ID)
        self.assertEqual(len(notes), 2)
        self.assertEqual(notes[0], TEST_NOTE)
        self.assertEqual(notes[1], note_2)

    def test_note_inserted_for_one_user_will_not_show_up_for_another_user(self):
        self.service.create_note(1, TEST_NOTE)

        notes = self.service.get_all_notes_by_user_id(2) # Different id!
        self.assertEqual(len(notes), 0)

    # TODO: Discuss
    def test_duplicate_notes_are_allowed(self):
        self.service.create_note(TEST_USER_ID, TEST_NOTE)
        self.service.create_note(TEST_USER_ID, TEST_NOTE)

        notes = self.service.get_all_notes_by_user_id(TEST_USER_ID)
        self.assertEqual(len(notes), 2)

# Tests for the Note class
class TestNote(unittest.TestCase):
    def test_two_same_objects_compare_equal(self):
        self.assertEqual(TEST_NOTE, TEST_NOTE)

    def test_two_separate_identical_objects_compare_equal(self):
        first = TEST_NOTE
        second = deepcopy(first)

        self.assertEqual(first, second)

    def test_two_unidentical_objects_compare_non_equal(self):
        first = TEST_NOTE
        second = deepcopy(first)
        second.year = "2010"

        self.assertNotEqual(first, second)

    def test_equality_comparison_against_different_object_type_returns_false(self):
        self.assertNotEqual(TEST_NOTE, "A string")