import random
import string

from repositories.note_repository import the_note_repository

class NoteService:
    def __init__(self, repository=the_note_repository):
        self._repository = repository

    def create_note(self, user_id, note):
        if not note.bib_citekey:
            note.bib_citekey = self.create_citekey()
        self._repository.create_note(user_id, note)
        return True

    def get_all_notes_by_user_id(self, user_id):
        return self._repository.get_all_notes_by_user_id(user_id)
    
    def check_if_citekey_exists(self, citekey):
        """Search from repository if the citekey already exists

        Args:
            citekey (string)

        Returns:
            Boolean: True if the citekey exists, False if not
        """
        return the_note_repository.check_if_citekey_exists(citekey)
    
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
    
    def create_citekey(self):
        """Create a new citekey. If one already exists, run the function again to create a new one.

        Returns:
            String: Random citekey
        """
        citekey = self._random_citekey()
        if self.check_if_citekey_exists(citekey):
            return self.create_citekey()
        return citekey
    
    
the_note_service = NoteService()
