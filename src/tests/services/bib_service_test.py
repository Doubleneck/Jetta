import unittest

from services.bib_service import the_bib_service
from repositories.note_repository import Note


valid_note_as_a_bib_str = '@' + 'book' + \
    '{' + 'author1999' + ',' + '\n\ttitle = {' + 'title' + '},' +\
    '\n\tauthor = {' + 'author' + '},' + '\n\tyear = {' + 'year' + '},' + \
    '\n\tdoi_address = {' + 'doi_address' + '}\n}' + '\n'

invalid_note_wrong_category = Note(bib_category='wrong_category', bib_citekey='author1999',
                                   author='author', title='title', year='year', doi_address='doi_address')

invalid_note_citekey_empty = Note(bib_category='wrong_category', bib_citekey='',
                                  author='author', title='title', year='year', doi_address='doi_address')


class TestBibService(unittest.TestCase):
    def setUp(self):
        self.service = the_bib_service
        self.valid_note = Note(bib_category='book', bib_citekey='author1999',
                               author='author', title='title', year='year', doi_address='doi_address')

    def test_bib_service_returns_a_str_with_valid_input(self):
        ret_type = type(self.service.generate_bib([self.valid_note]))
        self.assertTrue(ret_type == str)

    def test_generate_bib_returns_roughly_right_bibtex_form_with_a_valid_input(self):
        ret = self.service.generate_bib([self.valid_note])
        self.assertEqual(ret[0], '@')
        self.assertEqual(ret[-2], '}')
        self.assertEqual(ret[-1], '\n')

    def test_generate_bib_returns_correctly_when_valid_input_one_note(self):
        ret = self.service.generate_bib([self.valid_note])
        self.assertEqual(ret, valid_note_as_a_bib_str)

    def test_generate_bib_returns_a_string_when_valid_input_all_categories(self):
        ret_type = type(self.service.generate_bib([self.valid_note]))
        self.assertTrue(ret_type == str)

        self.valid_note.bib_category = 'article'
        ret_type = type(self.service.generate_bib([self.valid_note]))
        self.assertTrue(ret_type == str)

        self.valid_note.bib_category = 'phdthesis'
        ret_type = type(self.service.generate_bib([self.valid_note]))
        self.assertTrue(ret_type == str)

        self.valid_note.bib_category = 'misc'
        ret_type = type(self.service.generate_bib([self.valid_note]))
        self.assertTrue(ret_type == str)
