from repositories.note_repository import the_note_repository

class NoteService:
    def create_note(self, bib_citekey, bib_category, author, title, year, doi_address):
        try:
            the_note_repository.create_note(
                bib_citekey=bib_citekey,
                bib_category=bib_category,
                author=author,
                title=title,
                year=year,
                doi_address=doi_address
            )
            return True
        except:
            return False

    def get_all_notes_by_user_id(self):
        try:
            return the_note_repository.get_all_notes_by_user_id()
        except:
            return False

the_note_service = NoteService()
