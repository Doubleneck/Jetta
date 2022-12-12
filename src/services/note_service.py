import random
import string

from repositories.note_repository import the_note_repository
from services.bib_service import the_bib_service

class NoteService:
    def __init__(self, repository=the_note_repository):
        self._repository = repository

    def create_note(self, user_id, note):
        if not note.bib_citekey or note.bib_citekey.isspace():
            note.bib_citekey = self.create_citekey(user_id)
        self._validate_note(user_id, note)
        self._repository.create_note(user_id, note)
        return True

    def get_all_notes_by_user_id(self, user_id):
        return self._repository.get_all_notes_by_user_id(user_id)
    
    def _validate_note(self, user_id, note):
        valid_categories = ['book','article','phdthesis','misc']
        if not note.bib_category.lower() in valid_categories:
            raise ValueError("Bib category must be one of: book, article, phdthesis or misc")
        if self.citekey_exists(user_id, note.bib_citekey):
            raise ValueError("The citekey has to be unique. Please try again with another citekey.")

    def citekey_exists(self, user_id, citekey):
        """Search from repository if the citekey already exists in user's notes

        Args:
            citekey (string)

        Returns:
            Boolean: True if the citekey exists, False if not
        """
        return the_note_repository.check_if_citekey_exists(user_id, citekey)
    
    def _random_citekey(self):
        """Creates a random citekey with: 5 random letters and 4 random numbers

        Returns:
            string: random citekey
        """
        letters = string.ascii_letters
        numbers = string.digits
        letter_string = ("".join(random.choice(letters) for i in range(5)))
        numbers_string = ("".join(random.choice(numbers) for i in range(4)))
        return letter_string + numbers_string
    
    def create_citekey(self, user_id):
        """Create a new citekey. If one already exists, run the function again to create a new one.

        Returns:
            String: Random citekey
        """
        citekey_found = False
        while not citekey_found:
            citekey = self._random_citekey()
            if not self.citekey_exists(user_id, citekey):
                citekey_found = True
        return citekey

    def get_notes_as_bib(self, user_id):
        """Gets the notes for the user and generates
        a bibtex file from them.

        Returns:
            String: the bibtex file as a string.
        """
        notes = self.get_all_notes_by_user_id(user_id)
        return the_bib_service.generate_bib(notes)
        
    
        
    
    
the_note_service = NoteService()
