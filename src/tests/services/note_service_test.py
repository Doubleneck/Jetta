import unittest
from copy import deepcopy
from repositories.note_repository import Note

from services.note_service import NoteService
from tests.repositories.note_repository_test import create_test_note_repository

TEST_USER_ID = 1
VALID_TEST_NOTE = Note(
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

    def test_note_creation_succeeds_with_valid_input(self):
        self.assertTrue(self.service.create_note(TEST_USER_ID, VALID_TEST_NOTE))

    def test_note_creation_fails_with_invalid_bib_category_input(self):
        INVALID_TEST_NOTE = Note(
            bib_citekey = "Gregory2009",
            bib_category = "opinion",
            author = "Keith Gregory and Sue Morón-García",
            title = "Assignment submission, student behaviour and experience",
            year = "2009",
            doi_address = "10.11120/ened.2009.04010016",
        )
        self.assertRaises(ValueError, lambda : self.service.create_note(TEST_USER_ID, INVALID_TEST_NOTE))

    def test_note_creation_fails_with_not_unique_bib_category_under_one_user(self):
        self.assertTrue(self.service.create_note(TEST_USER_ID, VALID_TEST_NOTE))
        INVALID_TEST_NOTE = Note(
            bib_citekey = "Gregory2009",
            bib_category = "article",
            author = "Keith Gregory",
            title = "Some other title from the same year",
            year = "2009",
            doi_address = "10.11120/ened.2009.04084267",
        )
        self.assertRaises(ValueError, lambda : self.service.create_note(TEST_USER_ID, INVALID_TEST_NOTE))

    def test_user_notes_is_empty_before_creating_notes(self):
        notes = self.service.get_all_notes_by_user_id(TEST_USER_ID)
        self.assertEqual(len(notes), 0)

    def test_user_notes_has_length_1_after_inserting_one_note(self):
        self.service.create_note(TEST_USER_ID, VALID_TEST_NOTE)
        notes = self.service.get_all_notes_by_user_id(TEST_USER_ID)
        self.assertEqual(len(notes), 1)

    def test_note_can_be_fetched_once_created(self):
        self.service.create_note(TEST_USER_ID, VALID_TEST_NOTE)
        note = self.service.get_all_notes_by_user_id(TEST_USER_ID)[0]
        self.assertEqual(note, VALID_TEST_NOTE)

    def test_multiple_different_notes_can_be_inserted_for_same_user_id(self):
        self.service.create_note(TEST_USER_ID, VALID_TEST_NOTE)
        
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
        self.assertEqual(notes[0], VALID_TEST_NOTE)
        self.assertEqual(notes[1], note_2)

    def test_note_inserted_for_one_user_will_not_show_up_for_another_user(self):
        self.service.create_note(1, VALID_TEST_NOTE)

        notes = self.service.get_all_notes_by_user_id(2) # Different id!
        self.assertEqual(len(notes), 0)

    def test_citekey_is_generated_if_input_is_none(self):
        input_note = Note(
            bib_citekey = None,
            bib_category = "book",
            author = "Kurose J.F., Ross K.W.",
            title = "Computer Networkin: A Top Down Approach",
            year = "2015",
            doi_address = "10.1037/0022-3245.83.3.405",
        )
        self.service.create_note(TEST_USER_ID, input_note)
        notes = self.service.get_all_notes_by_user_id(TEST_USER_ID)
        test_note = notes[0]
        citekey = test_note.bib_citekey
        self.assertFalse(citekey is input_note.bib_citekey)
        self.assertTrue(isinstance(citekey, str))
        self.assertFalse(citekey.isspace())
        self.assertTrue(len(citekey) > 0)

    def test_citekey_is_generated_if_input_is_empty(self):
        input_note = Note(
            bib_citekey = "",
            bib_category = "book",
            author = "Kurose J.F., Ross K.W.",
            title = "Computer Networkin: A Top Down Approach",
            year = "2015",
            doi_address = "10.1037/0022-3245.83.3.405",
        )
        self.service.create_note(TEST_USER_ID, input_note)
        notes = self.service.get_all_notes_by_user_id(TEST_USER_ID)
        test_note = notes[0]
        citekey = test_note.bib_citekey
        self.assertFalse(citekey is input_note.bib_citekey)
        self.assertTrue(isinstance(citekey, str))
        self.assertFalse(citekey.isspace())
        self.assertTrue(len(citekey) > 0)

    def test_citekey_is_generated_if_input_is_space(self):
        input_note = Note(
            bib_citekey = "  ",
            bib_category = "book",
            author = "Kurose J.F., Ross K.W.",
            title = "Computer Networkin: A Top Down Approach",
            year = "2015",
            doi_address = "10.1037/0022-3245.83.3.405",
        )
        self.service.create_note(TEST_USER_ID, input_note)
        notes = self.service.get_all_notes_by_user_id(TEST_USER_ID)
        test_note = notes[0]
        citekey = test_note.bib_citekey
        self.assertFalse(citekey is input_note.bib_citekey)
        self.assertTrue(isinstance(citekey, str))
        self.assertFalse(citekey.isspace())
        self.assertTrue(len(citekey) > 0)

# Tests for the Note class
class TestNote(unittest.TestCase):
    def test_two_same_objects_compare_equal(self):
        self.assertEqual(VALID_TEST_NOTE, VALID_TEST_NOTE)

    def test_two_separate_identical_objects_compare_equal(self):
        first = VALID_TEST_NOTE
        second = deepcopy(first)

        self.assertEqual(first, second)

    def test_two_unidentical_objects_compare_non_equal(self):
        first = VALID_TEST_NOTE
        second = deepcopy(first)
        second.year = "2010"

        self.assertNotEqual(first, second)

    def test_equality_comparison_against_different_object_type_returns_false(self):
        self.assertNotEqual(VALID_TEST_NOTE, "A string")
