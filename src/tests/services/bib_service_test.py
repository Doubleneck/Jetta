import unittest

from services.bib_service import the_bib_service
from repositories.note_repository import Note


VALID_NOTE_AS_A_BIB_STR =  "@" + "book" + \
                "{" + 'author1999' + "," + "\n\ttitle = {" + 'title' + "}," +\
                "\n\tauthor = {" + 'author' + "}," + "\n\tyear = {" + 'year' + "}," + \
                "\n\tdoi_address = {" + 'doi_address' + "}\n}" + "\n"

INVALID_NOTE_WRONG_CATEGORY = Note(bib_category = 'wrong_category',bib_citekey ='author1999', \
    author= 'author', title = 'title', year = 'year', doi_address= 'doi_address')    

INVALID_NOTE_CITEKEY_EMPTY = Note(bib_category = 'wrong_category',bib_citekey ='', \
    author= 'author', title = 'title', year = 'year', doi_address= 'doi_address')  

class TestBibService(unittest.TestCase):
    def setUp(self):
        self.service = the_bib_service
        self.VALID_NOTE = Note(bib_category = 'book',bib_citekey ='author1999', \
        author= 'author', title = 'title', year = 'year', doi_address= 'doi_address')

    def test_bib_service_returns_a_str_with_valid_input(self):
        ret = self.service.generate_bib([self.VALID_NOTE])
        self.assertTrue(type(ret)is str)

    def test_generate_bib_returns_roughly_right_bibtex_form_with_a_valid_input(self):
        ret = self.service.generate_bib([self.VALID_NOTE])
        self.assertEqual(ret[0],'@')   
        self.assertEqual(ret[-2], '}')  
        self.assertEqual(ret[-1], '\n')  

    def test_generate_bib_returns_correctly_when_valid_input_one_note(self):
        ret = self.service.generate_bib([self.VALID_NOTE])
        self.assertEqual(ret, VALID_NOTE_AS_A_BIB_STR)     

    def test_generate_bib_returns_a_string_when_valid_input_all_categories(self):
        ret = self.service.generate_bib([self.VALID_NOTE])
        self.assertTrue(type(ret)is str)

        self.VALID_NOTE.bib_category = 'article'
        ret = self.service.generate_bib([self.VALID_NOTE])
        self.assertTrue(type(ret)is str)
        
        self.VALID_NOTE.bib_category = 'phdthesis'
        ret = self.service.generate_bib([self.VALID_NOTE])
        self.assertTrue(type(ret)is str)

        self.VALID_NOTE.bib_category = 'misc'
        ret = self.service.generate_bib([self.VALID_NOTE])
        self.assertTrue(type(ret)is str)

    def test_generate_bib_raises_value_error_if_wrong_bib_category_one_note(self):
        with self.assertRaises(ValueError):
            self.service.generate_bib([INVALID_NOTE_WRONG_CATEGORY])

    def test_generate_bib_raises_value_error_if_wrong_bib_category_in_one_note_list_of_two(self):
        with self.assertRaises(ValueError):
            self.service.generate_bib([self.VALID_NOTE,INVALID_NOTE_WRONG_CATEGORY])        

    def test_generate_bib_raises_value_error_if_citekey_empty_list_of_two(self):
        with self.assertRaises(ValueError):
            self.service.generate_bib([self.VALID_NOTE,INVALID_NOTE_CITEKEY_EMPTY]) 
       
    def test_validate_note_returns_true_if_valid_note(self):
        self.assertTrue(self.service.validate_note(self.VALID_NOTE))

    def test_validate_note_returns_false_if_invalid_note_wrong_category(self):
        with self.assertRaises(ValueError):
            self.service.validate_note(INVALID_NOTE_WRONG_CATEGORY)

    def test_validate_note_returns_false_if_invalid_note_empty_citekey(self):
        with self.assertRaises(ValueError):
            self.service.validate_note(INVALID_NOTE_CITEKEY_EMPTY)  